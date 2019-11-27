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
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
CORS(app)

q = Queue(connection=Redis())

@app.route('/ping', methods=['GET'])
def ping_pong():
    print(request)
    return jsonify('pong!')

#Queue the split process and respond to the request
def split_audio(filename, stem):
    song_folder = filename.rsplit('.', 1)[0]
    print(song_folder)
    output_dir = Path(OUTPUT_FOLDER)
    #split.split(str(Path(app.config['UPLOAD_FOLDER']) / filename), str(output_dir), int(stem))
    q.enqueue(split.split, str(Path(app.config['UPLOAD_FOLDER']) / filename), str(output_dir), int(stem))
    output_files = dict()
    if stem == 2:
        output_files['voice'] = song_folder + '/vocals.wav'
        output_files['other'] = song_folder + '/accompaniment.wav'
    if stem == 4 or stem == 5:
        output_files['voice'] = song_folder + '/vocals.wav'
        output_files['other'] = song_folder + '/other.wav'
        output_files['drums'] = song_folder + '/drums.wav'

        output_files['bass'] = song_folder + '/bass.wav'
    if stem == 5:
        output_files['piano'] = song_folder + '/piano.wav'
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
        if 'stem' not in request.form:
            return 'Please specify a number of stem in your query'
        stem = int(request.form['stem'])
        if stem != 2 and stem != 4 and stem != 5:
           return 'Wrong stem value'
        if file and allowed_file(file.filename) and request.form['stem']:
            filename = secure_filename(file.filename)
            file_path = Path(app.config['UPLOAD_FOLDER']) / filename
            file.save(str(file_path))
            print (filename)
            ret = split_audio(filename, stem)
            return jsonify(ret)
        else:
            return "Wrong file format. Only '.mp3' accepted."
    return "Upload successfull"

#Serve files in the output folder
@app.route('/file/<path:path>')
def get_file(path):
    print(path)
    try:
        return send_from_directory(app.config['OUTPUT_FOLDER'], path)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=int("5050"))