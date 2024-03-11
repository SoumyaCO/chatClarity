from flask import Flask, request, render_template, flash, redirect, url_for 
from werkzeug.utils import secure_filename
from flask_cors import CORS
import pandas as pd
import plotly.express as px
from flask_utils import get_and_preprocess_data, handle_file_errors
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
CORS(app)  
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.get("/query")
# def show_form():
#     return <h1>Go to the https://localhost:5000/query</h1>


# @app.post('/')
# def get_data():
#     if 'file' not in request.files:
#         flash("No file part in the request")
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash("No file selected")
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#     # handover the file to the get_and_preprocess_data function
#         get_and_preprocess_data(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         os.remove(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         return render_template('plot.html'), 200

#     else:
#         flash("Invalid file")
#         return redirect(request.url)

@app.get('/query')
def get_data_and_date():
    return render_template('index.html'), 200

@app.post('/query')
def process_query():
    handle_file_errors(request)
    file = request.files['file']
    date = request.form['datetime']
    if file and date and allowed_file(file.filename):
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(upload_path)
        get_and_preprocess_data(upload_path, date)
        os.remove(upload_path)
        return render_template('plot.html'), 200

    




if __name__ == '__main__':   
    app.run(debug=True)


# USAGE
# check .env is activated or not
# check you're in experimentations_flask folder
# python3 flask_app.py