'''
Contains everythng related to data [ingestion, processing, and plotting]
'''
# Imports ________________________________
import pandas as pd
import plotly.express as px
import re


# data processing functions ___________________________________

# Split Date_Time into Date and Time (converts 'Date' into 'datetime' format)
def split_and_format(data: pd.DataFrame) -> pd.DataFrame:
    """
    Process the given DataFrame by splitting the 'Date_Time' column into separate 'Date' and 'Time' columns,
    dropping the 'Time' and 'Date_Time' columns, and converting the 'Date' column to datetime format.

    Args:
        data (pd.DataFrame): The input DataFrame to be processed.

    Returns:
        pd.DataFrame: The processed DataFrame with the 'Date_Time' column split and converted to datetime format.
    """
    data[["Date", "Time"]] = data["Date_Time"].str.split(',', expand=True)
    data.drop(["Time", "Date_Time"], axis=1, inplace=True)
    data["Date"] = pd.to_datetime(data["Date"], format="mixed")
    return data


# [FOR NOW] preprocess the data and generated a histogram plot
def process_data(path: str, date) -> None:
    """
    Reads a file from the given path, preprocesses the data, and generates a histogram plot.

    Args:
        path (str): The path to the file to be read.
        date: The date to filter the data.

    Returns:
        None
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
            df = split_and_format(data=df)
            px.histogram(df[df["Date"] < date], x="User", title="User vs Message Count").write_html("templates/plot.html")
    except:
        print("No such file.")

