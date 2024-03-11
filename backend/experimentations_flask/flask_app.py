from flask import Flask, request, render_template, flash, redirect, url_for 
from werkzeug.utils import secure_filename
from flask_cors import CORS
import pandas as pd
import plotly.express as px
from flask_utils import get_and_preprocess_data, plot_some_data, delete_plot
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
CORS(app)  
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/")
def show_form():
    return render_template('index.html'), 200


@app.post('/')
def get_data():
    if 'file' not in request.files:
        flash("No file part in the request")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash("No file selected")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        return render_template('success.html')
        # data = get_and_preprocess_data(file)
        # plot_some_data(data)
        # return render_template('plot.html'), 200
    else:
        flash("Invalid file")
        return redirect(request.url)



if __name__ == '__main__':   
    app.run(debug=True)


# USAGE
# check .env is activated or not
# check you're in experimentations_flask folder
# python3 flask_app.py