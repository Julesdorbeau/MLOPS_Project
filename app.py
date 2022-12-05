from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
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
            if r_form == 'Default (TFlite)':
                print(r_form)
                return render_template('index.html', transcript=r_form)

            elif r_form == 'Default (h5)':
                print(r_form)
                return render_template('index.html', transcript=r_form)
            
            elif r_form == 'Experimental (TFlite)':
                print(r_form)
                return render_template('index.html', transcript=r_form)
            
            elif r_form == 'Float 16 (TFlite)':
                print(r_form)
                return render_template('index.html', transcript=r_form)
            
            elif r_form == 'No optimization (TFlite)':
                print(r_form)
                return render_template('index.html', transcript=r_form)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    
