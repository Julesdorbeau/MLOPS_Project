from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = "*waiting for audio*"
    if request.method == "POST":
        #has_changed = 0
        transcript = "*waiting for audio*"
        print("Variable transcript set to: (BEGIN):", transcript)
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            print("No file?")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            print("No filename?")
            return redirect(request.url)

        if file:
            print("File", file.filename, "has been loaded")
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            has_changed = 1
        print("Variable transcript set to: (END):", transcript)
            
    #if has_changed == 0:
        #transcript="*waiting for audio*"
    print("Variable transcript set to: (EOF):", transcript)
    return render_template('index.html', transcript=transcript)

    
    
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    
