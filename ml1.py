import pandas as pd
import yfinance as yf
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#download google stock data into a dataframe
df = yf.download('GOOG', start='2024-01-01', end='2024-12-31', auto_adjust=True)

# print(df.head())

#default columns
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
df.rename(columns={
    'Open': 'Adj. Open',
    'High': 'Adj. High',
    'Low': 'Adj. Low',
    'Close': 'Adj. Close',
    'Volume': 'Adj. Volume'
}, inplace=True)

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0 #volatility
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0 #daily % change

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

#returns headers and a specific number of rows starting at the top, opp -> .tail()
# print(df.head())

scaler = StandardScaler()

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) #replace missing data
"""
len(df) = 366days - 113days(weekends + public holidays) = 253
"""
forecast_out = int(math.ceil(0.01*len(df))) # 3days

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
# print(df.tail())

x = np.array(df.drop(columns=['label']))
y = np.array(df['label'])

#scaling x
x = scaler.fit_transform(x)

# print(df.tail())

x = x[:-forecast_out+1]

df.dropna(inplace=True)
y = np.array(df['label'])

print(len(x), len(y))