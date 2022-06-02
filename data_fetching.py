# Sourcing the data
# Load libraries
import pandas as pd
import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import csv
# Yahoo for dataReader
import yfinance as yf
yf.pdr_override()

import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Load dataset


def get_data_from_yahoo():
    tickers = ['AAPL','MSFT','INTC','AMZN','GS','SPY','GDX','GLD']
    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()
    dataset = yf.download(tickers, start=start, end=end)['Close']
    print('dataset \n', dataset.tail(10))
    dataset.to_csv("tickers_data.csv")
    return dataset.to_csv("tickers_data.csv")

get_data_from_yahoo()
