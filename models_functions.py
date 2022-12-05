import glob
import pathlib
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import tflite_runtime.interpreter
import time

label_names = ['down' 'go' 'left' 'no' 'right' 'stop' 'up' 'yes']

# ===== Preprocessing functions =====

def get_spectrogram(waveform):
    # Convert the waveform to a spectrogram via a STFT.
    spectrogram = tf.signal.stft(waveform, frame_length=255, frame_step=128)
    # Obtain the magnitude of the STFT.
    spectrogram = tf.abs(spectrogram)
    # Add a `channels` dimension, so that the spectrogram can be used
    # as image-like input data with convolution layers (which expect
    # shape (`batch_size`, `height`, `width`, `channels`).
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram

def preprocess_audio(audio) : 
    # Function used to preprocess our audio and make it usable by our models
    x, sample_rate = tf.audio.decode_wav(audio, desired_channels=1, desired_samples=16000,)
    x = tf.squeeze(x, axis=-1)
    waveform = x
    x = get_spectrogram(x)
    x = x[tf.newaxis,...]
    return x

# ===== Flask call functions for prediction =====

def run_tflite_prediction(model_path, audio) : 
    # Function to run the prediction with an tflite model
    interpreter = tflite_runtime.interpreter.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], audio)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    predicted_label = np.argmax(prediction[0])
    
    # Used to display the plot of the prediction
    # plt.bar(label_names, tf.nn.softmax(prediction[0]))
    # plt.title('Predictions')
    # plt.show()
    print(predicted_label)
    return predicted_label

def run_normal_prediction(model_path, audio) :
    model = keras.models.load_model(model_path)
    prediction = model(audio)
    predicted_label = np.argmax(prediction[0])
    # Used to display the plot of the prediction
    # plt.bar(label_names, tf.nn.softmax(prediction[0]))
    # plt.title('Predictions')
    # plt.show()
    print(predicted_label)
    return predicted_label

def run_model_prediction(model_path, audio) : 
    preprocessed_audio = preprocess_audio(audio)
    if "h5" in model_path :
        run_normal_prediction(model_path, preprocessed_audio)
    elif "tflite" in model_path :
        run_tflite_prediction(model_path, preprocessed_audio)
    else : 
        print("Cannot use a model that is not a .h5 or .tflite model. Stopping program.")

# ===== Testsuites functions

def get_audio(filename) :
    x = tf.io.read_file(filename)

    # Getting the true label
    split_name = filename.split("-")
    label = int(split_name[0][-1])

    x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000,)
    x = tf.squeeze(x, axis=-1)
    waveform = x
    x = get_spectrogram(x)
    x = x[tf.newaxis,...]
    return x, label

def run_normal_testsuite(model_path, filenames) :
    true_labels = []
    predicted_labels = []
    time_count = 0

    model = keras.models.load_model(model_path)

    for filename in filenames:
        audio_data, label = get_audio(filename)

        # Setting a time to get the time for the prediction and get a mean of the time on the rasp
        start_time = time.time()

        prediction = model(audio_data)
        
        # End of the prediction time
        end_time = time.time()

        # Adding this to the timer counter
        time_count += (end_time - start_time)

        # Getting the prediction
        predicted_label = np.argmax(prediction[0])

        # Appending the true label and prediction to determine the accuracy
        predicted_labels.append(predicted_label)
        true_labels.append(label)

    predicted_labels = np.array(predicted_labels)
    true_labels = np.array(true_labels)
    accuracy = (true_labels == predicted_labels).mean()
    mean_time = time_count / len(true_labels)
    print("Accuracy on test set for {0} : {1}. Predictions took in average {2}s.".format(model_path, accuracy, mean_time))
    
def run_tflite_testsuite(model_path, filenames) :
    true_labels = []
    predicted_labels = []
    time_count = 0

    interpreter = tflite_runtime.interpreter.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    for filename in filenames:
        audio_data, label = get_audio(filename)

        # Setting a time to get the time for the prediction and get a mean of the time on the rasp
        start_time = time.time()

        interpreter.set_tensor(input_details[0]['index'], audio_data)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])
        
        # End of the prediction time
        end_time = time.time()

        # Adding this to the timer counter
        time_count += (end_time - start_time)

        # Getting the prediction
        predicted_label = np.argmax(prediction[0])

        # Appending the true label and prediction to determine the accuracy
        predicted_labels.append(predicted_label)
        true_labels.append(label)

    predicted_labels = np.array(predicted_labels)
    true_labels = np.array(true_labels)
    accuracy = (true_labels == predicted_labels).mean()
    mean_time = time_count / len(true_labels)
    print("Accuracy on test set for {0} : {1}. Predictions took in average {2}s.".format(model_path, accuracy, mean_time))

def run_testsuite(model_path) : 
    filenames = glob.glob('data/*/*')
    if "h5" in model_path :
        run_normal_testsuite(model_path, filenames)
    elif "tflite" in model_path :
        run_tflite_testsuite(model_path, filenames)
    else : 
        print("Cannot use a model that is not a .h5 or .tflite model. Stopping program.")

def run_all_models_testsuite() :
    run_testsuite("models/normal_model.h5")
    run_testsuite("models/model_default.tflite")
    run_testsuite("models/model_no_opti.tflite")
    run_testsuite("models/model_experimental.tflite")
    run_testsuite("models/model_float16.tflite")

# run_all_models_testsuite()