import pandas as pd
import matplotlib.pyplot as plt
"""
dataframe - 2-dimensional data structure like 2-d array
:::::- (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
"""
####

data = {
  "runner": ['fred', 'mwaura', 'john'],
  "score": [50, 34, 45]
}

df = pd.DataFrame(data)
# print(df)
#indices

# print(df.loc[0])

#loading CSV into a dataframe

#default = 60
pd.options.display.max_rows = 99999 

df_read = pd.read_csv('data.csv')

# print(df_read)

#loading JSOn into a dataframe
df_json  = pd.read_json('data.json')
# print(df_json.to_string())
# print(df_json.info())

"""
cleaning data - removing bad data sets
- empty cells - replace or remove
- data in wrong format - remove or convert all cells to same format
- Wrong data
- Duplicates
"""
# using the csv dataframe

new_df = df_json.dropna() #removing rows that contain bad datasets
# print(new_df.to_string())

# modifying the original dataframe since by default it returns a new dataframe
df_json.dropna(inplace=True)

# replacing the empty values
df_json.fillna(-9999, inplace=True)
df_json.fillna({'calories': -9999}, inplace=True) #replacing specified columns
# using mean, median and mode => functions

x = df_json["Calories"].mean() # rep - .median(), .mode()[0]
"""
mode() -> returns a list of all modes from the most repeated hence .mode()[0]
"""
df.fillna({"Calories": x}, inplace=True)

#cleaning wrong- format
df_json = pd.read_json('data.json')
#df_json['Date] - line 26('20201226')
print(df_json.columns)

# df_json['Date'] = pd.to_datetime(df_json['Date'], format='mixed') # returns formated date - '2020/12/26

# #removing wrong data
# df_json.dropna(subset=['Date'], inplace=True)

"""
wrong data - out of expectation - wild
"""

df_json.loc[7, 'Duration'] = 45

#for instance of multiple wrong data:
#duration expected should be less than 120mins

# loop over
for x in df_json.index:
  if df_json.loc[x, "Duration"] > 120:
    df_json[x, "Duration"] = 120
#removing rows with the wrong data:

for x in df_json.index:
  if df_json.loc[x, "Duration"] > 120:
    df_json.drop(x, inplace=True)
    
#Duplicates

# check 
print(df_json.duplicated()) # True for duplicates else False

df_json.drop_duplicates(inplace=True)

"""
correlations -> quatifies the degree to which two variables are related to each other
corr() calculates the correlation between each column in a dataset
corr - ignores non numeric columns
1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
"""
#recap
df__csv = pd.read_csv('data.csv')
# print(df__csv.to_string())
# df__csv.plot()
# plt.show()
# print(df__csv.corr())

"""
kind - scatter, hist
"""
df__csv.plot(kind = 'hist', x = 'Duration', y = 'Maxpulse')

plt.show()