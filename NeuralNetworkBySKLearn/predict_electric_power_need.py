# script to practice neural network transcribed from
# https://qiita.com/mix_dvd/items/1f96f5202614dbea93e0

# data taken from
# https://www.tepco.co.jp/forecast/html/download-j.html
# https://www.data.jma.go.jp/gmd/risk/obsdl/index.php

# record command history in IPython by
# %history -f [filename]
# run by
# %run ./[filename]

import pandas as pd
import numpy as np
import datetime as dt
import math
filename = "juyo-2014.csv"

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# pandas read_csv recognizes the first row as column index; to avoid it, use header=None option
df = pd.read_csv(filename,encoding="SHIFT_JIS",skiprows=2)
df.columns = ["DATE","TIME","KW"]
df.index = df.index.map(lambda x: dt.datetime.strptime(df.loc[x].DATE + " "+ df.loc[x].TIME,"%Y/%m/%d %H:%M"))
df["MONTH"] = df.index.month
df["WEEK"] = df.index.weekday
df["HOUR"] = df.index.hour
df_kw = df
filename = "data-2014.csv"
df = pd.read_csv(filename,encoding="SHIFT-JIS")
df_temp = df[["a","b"]]
df_temp.columns = ["DATE","TEMP"]
df_temp.index = df_temp.index.map(lambda x: dt.datetime.strptime(df_temp.loc[x].DATE,"%Y/%m/%d %H:%M:%S"))
d1 = df_kw.index.min()
d2 = df_kw.index.max()
df_kw["TEMP"] = df_temp.loc[d1:d2].TEMP
X_cols = ["MONTH","WEEK","HOUR","TEMP"]
y_cols = ["KW"]
X = df_kw[X_cols].to_numpy().astype('float')
y = df_kw[y_cols].to_numpy().astype('int').flatten()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=42)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
print(model.score(X_test,y_test))

