import pandas as pd
import re
import plotly.express as px
from flask import redirect, flash

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess dataframe: returns dataframe with 3 columns (date, user, message)

    Parameter
    ---------
    data: pandas.DataFrame

    Returns
    -------
    data: pandas.DataFrame
    """
    data[["Date", "Time"]] = data["Date_Time"].str.split(',', expand=True)
    data.drop(["Time", "Date_Time"], axis=1, inplace=True)
    data["Date"] = pd.to_datetime(data["Date"], format="mixed")
    return data

def get_and_preprocess_data(path: str, date) -> None:
    """
    Get the data from a path and preprocess it

    Parameters
    ----------
    path: location of the .txt file (chat)

    Returns
    -------
    df: pandas.DataFrame
    """
    try:
        with open(path) as file:
            content = file.read()
            pattern = r"(.*?) \- (.*?): (.*)|\[(.*?)\] (.*?): (.*)"
            matches = re.findall(pattern, content)
            df = pd.DataFrame(matches, columns=["Date_Time", "User", "Message", "Date_Time", "User", "Message"])

            # trimming the
            df.replace("", float("NaN"), inplace=True)
            df.dropna(how='all', axis=1, inplace=True)
            df = process_data(data=df)
            px.histogram(df[df["Date"] < date], x="User", title="User vs Message Count").write_html("templates/plot.html")
    except:
        print("No such file. ")

def handle_file_errors(request):
    if 'file' not in request.files:
        flash("No file part in the request")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash("No file selected")
        return redirect(request.url)