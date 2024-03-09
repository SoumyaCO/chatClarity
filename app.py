import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
warnings.filterwarnings('ignore')

from utils import get_and_preprocess_data


def get_snapshot():
    path = input("Enter the path: ")
    df = get_and_preprocess_data(path)
    print(df.head())



if __name__ == "__main__":
    get_snapshot()
