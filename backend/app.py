'''
API routes and main file to run 
'''
import os
from flask import request, render_template, redirect, json
from werkzeug.utils import secure_filename
from config import app, UPLOAD_FOLDER
from utils import allowed_file
from data_processing import process_data, user_vs_msg_count

# Routes
# tesing =================
@app.post('/test')       
def test_route():          
    data = request.form
    date = data['date']
    file = request.files['file']
    upload_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(upload_path)
    message = user_vs_msg_count(upload_path)
    return json.dumps(message), 200
    

                         
# testng =================

@app.get('/')
def got_to_query():
    return "<a href='http://localhost:5000/query'> Go here </a>"

#query route
@app.get('/query')
def get_data_and_date():
    return render_template('index.html'), 200

@app.post('/query')
def process_query():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    file = request.files['file']
    date = request.form['datetime']
    if file and date and allowed_file(file.filename):
        upload_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(upload_path)
        process_data(upload_path, date)
        os.remove(upload_path)
        return render_template('plot.html'), 200

    















# @app.get("/query")
# def show_form():
#     return <h1>Go to the https://localhost:5000/query</h1>


# @app.post('/')
# def get_data():
    # if 'file' not in request.files:
    #     return redirect(request.url)
    # file = request.files['file']
    # if file.filename == '':
    #     return redirect(request.url)
#     if file and allowed_file(file.filename):
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#     # handover the file to the get_and_preprocess_data function
#         get_and_preprocess_data(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         os.remove(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         return render_template('plot.html'), 200

#     else:
#         flash("Invalid file")
#         return redirect(request.url)
    

    
if __name__ == '__main__':   
    app.run(debug=True)