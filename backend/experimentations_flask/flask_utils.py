import pandas as pd
import re
import matplotlib.pyplot as plt
import os
import plotly.express as px

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

def get_and_preprocess_data(path: str) -> None:
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
            px.histogram(df[df["Date"] > '30-01-2024'], x="User", title="User vs Message Count").write_html("templates/plot.html")
    except:
        print("No such file. ")


# DUMMY FUNCTION FOR CHECKING
def plot_some_data(data: pd.DataFrame):
    data.User.plot.bar()
    plt.savefig('templates/plot.html')

def delete_plot():
    if os.path.exists('templates/plot.html'):
        os.remove('templates/plot.html')
    else:
        print("The file does not exist")