'''
Contains everythng related to data [ingestion, processing, and plotting]
'''
# Imports ________________________________
import pandas as pd
import plotly.express as px
import re
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')


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


# preprocess the data and return clean dataframe
def process_data(path: str) -> None:
    """
    Reads a file from the given path, preprocesses the data

    Args:
        path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame
    """
    # try:
    with open(path,encoding='utf-8') as file:
        content = file.read()
        pattern = r"(.*?) \- (.*?): (.*)|\[(.*?)\] (.*?): (.*)"
        matches = re.findall(pattern, content)
        df = pd.DataFrame(matches, columns=["Date_Time", "User", "Message", "Date_Time", "User", "Message"])
            # trimming extra columns
        df.replace("", float("NaN"), inplace=True)
        df.dropna(how='all', axis=1, inplace=True)
        df = split_and_format(data=df)
            # making the messages into right format
        df.Message = df.Message.apply(lambda x: x.encode('ascii', 'ignore').decode('utf-8'))
            # making the user into right format
        df.User = df.User.apply(lambda x: x.encode('ascii', 'ignore').decode('utf-8'))
    print(df)
    return df
    # except:
    #     print("[data_processing.py/process_data()] Not a an appropriet file.")


def date_vs_msg_count(path: str):
    data = process_data(path)
    sorted_df = data.sort_values(by='Date')
    date_message_count = sorted_df["Date"].value_counts().reset_index()
    dates = date_message_count.Date.dt.date.values.tolist()
    count = date_message_count["count"].values.tolist()
    message = {
        'dates': dates[:10],
        'count': count[:10]
    }
    return message

def user_vs_msg_count(path: str):

    # try:
    data = process_data(path)
    users = data['User'].value_counts().reset_index()['User'].values.tolist()
    counts = data['User'].value_counts().reset_index()['count'].values.tolist()
    message = {
        'users': users[:10],
        'counts': counts[:10]
    }
    print(message)
    return message
    # except:
    #     print("[data_processing.py/user_vs_msg_count()] Something Fishy.")


