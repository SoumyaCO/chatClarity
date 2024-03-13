'''
Flask app configurations, upload files, api routes and all
'''
from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
CORS(app)

app.secret_key = "KPSUgmaRRnaP2P0i"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

