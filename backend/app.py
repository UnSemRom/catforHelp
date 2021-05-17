from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from werkzeug.utils import secure_filename
import os
import urllib.request
from txt_handler import TextHandlerFrequency, TextHandlerCloud, TextHandlerSemantic
import json
import matplotlib.pyplot as plt
import base64
import os.path
from flask_cors import CORS

UPLOAD_FOLDER = '../files'
# ../ - выходит из этой папки и заходит в files

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

client = app.test_client()

#создаем базу данных
engine = create_engine('sqlite:///db.sqlite')

#создаем сессию
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)
cors = CORS(app)

from models import *

Base.metadata.create_all(bind = engine)

ALLOWED_EXTENSIONS = set(['txt'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/multiple-files-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 206
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
       
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

@app.route('/comparison_frequency_analysis', methods=['POST','GET'])
def comparison_frequency_analysis():
    txthandler = TextHandlerFrequency()
    files = request.files.getlist('files[]')

    textes = []

    for file in files:
        text_from_file = file.read().decode()
        textes.append(text_from_file)

    result = txthandler.comparison_frequency_analysis_str(textes)
    return result
    #return json.dumps(result, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

@app.route('/frequency_analysis', methods=['POST','GET'])
def frequency_analysis():
    txthandler = TextHandlerFrequency()

    files = request.files.getlist('files[]')
    
    textes = []
    
    for file in files:
        #filename = secure_filename(file.filename)
        text_from_file = file.read().decode()
        textes.append(text_from_file)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #textes.append(filename)

    result = txthandler.frequency_analysis(textes)
    return result

@app.route('/get_all_user_files/<user_id>', methods=['GET'])
def get_all_user_files(user_id):

    return 200

@app.route('/semantic_analysis', methods=['POST','GET'])
def semantic_analysis():
    txthandler = TextHandlerSemantic()

    files = request.files.getlist('files[]')

    textes = []

    for file in files:
        text_from_file = file.read().decode()
        textes.append(text_from_file)

    result = txthandler.semantic_analysis(textes)

    return json.dumps(result, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

@app.route('/get_tf_idf_query_similarity', methods=['POST','GET'])
def get_tf_idf_query_similarity():
    txthandler = TextHandlerSemantic()

    files = request.files.getlist('files[]')

    textes = []

    for file in files:
        text_from_file = file.read().decode()
        textes.append(text_from_file)

    result = txthandler.get_tf_idf_query_similarity(textes)

    #js_result = result.to_json(force_ascii=False)
    return result

@app.route('/WordCloud', methods=['POST','GET'])
def WordCloud():
    txthandler = TextHandlerCloud()

    files = request.files.getlist('files[]')

    textes = []

    for file in files:
        text_from_file = file.read().decode()
        textes.append(text_from_file)

    result = txthandler.WordCloud(textes)
    result_base64image = {}

    for i in range(len(files)+1):
        plt.imshow(result[i], interpolation='bilinear')
        plt.axis("off")
        plt.savefig('saved_figure.png')
        image = open('saved_figure.png', 'rb')
        image_read = image.read()
        base64image_b = base64.b64encode(image_read)
        base64image = base64image_b.decode('utf-8')
        result_base64image["Text"+str(i)] = base64image
        image.close()
        plt.close()
        os.remove("D:\FatData-analysis\FatData-analysis\CATsite\Backend\saved_figure.png")

    return result_base64image

@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}

@app.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

if __name__ == '__main__':
    app.run()