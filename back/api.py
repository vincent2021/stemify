import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path
from werkzeug.utils import secure_filename
from zipfile import ZipFile
import split
from redis import Redis
from rq import Queue

#Configuration and Ping route

UPLOAD_FOLDER = 'raw_data'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="template")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

q = Queue(connection=Redis())

@app.route('/ping', methods=['GET'])
def ping_pong():
    print(request)
    return jsonify('pong!')

#Get stems
def split_audio(filename, stem):
    song_folder = filename
    output_dir = Path(OUTPUT_FOLDER) / song_folder
    #split.split(str(Path(app.config['UPLOAD_FOLDER']) / filename), str(output_dir), int(stem))
    q.enqueue(split.split, str(Path(app.config['UPLOAD_FOLDER']) / filename), str(output_dir), int(stem))
    if stem == 2:
        output_files = {"voice" : song_folder + '/vocals.wav', "accompaniment": song_folder + '/accompaniment.wav'}
    return output_files

#Upload a file and convert it
@app.route('/upload', methods=['POST'])
def save_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print(request.files)
            return 'No file'
        file = request.files['file']
        if file.filename == '':
            return 'No filename'
        if file and allowed_file(file.filename) and request.form['stem']:
            filename = secure_filename(file.filename)
            file_path = Path(app.config['UPLOAD_FOLDER']) / filename
            file.save(str(file_path))
            stem = int(request.form['stem'])
            ret = split_audio(filename, stem)
            return jsonify(ret)
        else:
            return "Wrong file format. Only '.mp3' accepted."
    return "Upload successfull"

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=int("5050"))