from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
import plotly.express as px
from flask_utils import get_and_preprocess_data, plot_some_data, delete_plot
import os

app = Flask(__name__)
# To handle Cross-Origin Resource Sharing (CORS)
CORS(app)  

# Initialize an empty DataFrame variable

@app.get("/")
def show_form():
    return render_template('index.html'), 200


@app.post('/')
def get_data():
    if 'file' not in request.files:
        return "No file part in the request", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    if file:
        return render_template('success.html')
        # data = get_and_preprocess_data(file)
        # plot_some_data(data)
        # return render_template('plot.html'), 200



if __name__ == '__main__':   
    app.run(debug=True)


# USAGE
# check .env is activated or not
# check you're in experimentations_flask folder
# python3 flask_app.py