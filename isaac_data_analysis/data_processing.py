import numpy as np
import pandas as pd
import talib
import matplotlib.pyplot as plt
import signal_analysis as sig
get_ipython().magic('matplotlib inline')

def find_extrema(df):
    close = np.array(df['close'])
    loc_max, loc_min = sig.find_local_extrema(close)
    return loc_max, loc_min

def get_data(filename, index_col, close_col):

    #import data from csv file
    dates = np.genfromtxt(filename, delimiter=',', dtype='str', skip_header=1, usecols=(index_col), unpack=True)
    close = np.genfromtxt(filename, delimiter=',', dtype='float', skip_header=1, usecols=(close_col), unpack=True)

    #data frame column names
    columns = ['close', 'rsi (14)', 'macd', 'macd signal', 'bol_upper (20)', 'bol_lower (20)', 'sma50', 'sma100', 'sma200']

    #create empy data frame, fill nans with 0
    df = pd.DataFrame(index=dates, columns=columns)
    df = df.fillna(0)

    rsi14 = talib.RSI(close, timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    upper_bol, middle_bol, lower_bol = talib.BBANDS(close, timeperiod=20)


    sma50  = talib.MA(close, timeperiod=50)
    sma100 = talib.MA(close, timeperiod=100)
    sma200 = talib.MA(close, timeperiod=200)

    df['close']            = close
    df['rsi (14)']         = rsi14
    #normalize macd and macd signal
    df['macd']             = macd
    df['macd signal']      = macd_signal
    df['bol_upper (20)']   = upper_bol
    df['bol_lower (20)']   = lower_bol
    df['sma50']            = sma50
    df['sma100']           = sma100
    df['sma200']           = sma200

    df = df.fillna(method='backfill')

    return df
