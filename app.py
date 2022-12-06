from flask import Flask, render_template, request, redirect#, jsonify
import speech_recognition as sr
import os
#import sounddevice
#from scipy.io.wavfile import write
from models_functions import *

app = Flask(__name__)


"""mfcc = 13   
size_of_chunks = 10000
n_fft = 2048
hop_length = 512"""


@app.route("/", methods=["GET", "POST"])
def index():
    label_names = ["down", "go", "left", "no", "right", "stop", "up", "yes"] 
    transcript = "*waiting for audio*"
    print("Variable transcript set to: (BEGIN):", transcript)
    
    if request.method == "POST":
        if "file" not in request.files:
            print("No file?")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            print("No filename?")
            return redirect(request.url)

        if file:
            print("File", file.filename, "has been loaded")
            data = request.files['file'].read()
            try:
                os.remove('input/myfile.wav')
            except OSError:
                pass
            with open('input/myfile.wav', mode='bx') as f:
                f.write(data)
                print("Audio file created in input/ file")
            r_form = request.form['submit_button']

            if r_form == 'Default (h5)':
                res = run_model_prediction("models/normal_model.h5", "input/myfile.wav")
                return render_template('index.html', transcript=label_names[res])

            elif r_form == 'Default (TFlite)':
                res = run_model_prediction("models/model_default.tflite", "input/myfile.wav")
                return render_template('index.html', transcript=label_names[res])
            
            elif r_form == 'Experimental (TFlite)':
                res = run_model_prediction("models/model_experimental.tflite", "input/myfile.wav")
                return render_template('index.html', transcript=label_names[res])
            
            elif r_form == 'Float 16 (TFlite)':
                res = run_model_prediction("models/model_float16.tflite", "input/myfile.wav")
                return render_template('index.html', transcript=label_names[res])
            
            elif r_form == 'No optimization (TFlite)':
                res = run_model_prediction("models/model_no_opti.tflite", "input/myfile.wav")
                return render_template('index.html', transcript=label_names[res])

    return render_template('index.html', transcript=transcript)


@app.route("/record")   
def record():
   print('Recording')
   return "Nothing"
   """fs = 22050
   seconds = 10
   record_voice = sounddevice.rec(int(seconds * fs), samplerate = fs, channels = 1, blocking = False)
   sounddevice.wait()
   write("recorded/recorded.wav", fs, record_voice)
   return jsonify(result="preds", answer = "words") """


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    
