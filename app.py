from flask import *
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = 'resume-summarizer/static/files/'  
  
@app.route('/') 
def main(): 
    return render_template("index.html") 
  
  
@app.route('/upload', methods=['POST']) 
def upload(): 
    if request.method == 'POST': 
  
        # Get the list of files from webpage 
        files = request.files.getlist("file") 
  
        # Iterate for each file in the files List, and Save them 
        for file in files:
            filename = secure_filename(file.filename) 
            file.save(app.config['UPLOAD_FOLDER'] + filename) 
        status = subprocess.run(["python","resume-summarizer/parser.py"], shell=True)
        print(status)
        return "<h1>Files Uploaded Successfully!</h1>"



if __name__ == '__main__': 
    app.run(debug=True) 