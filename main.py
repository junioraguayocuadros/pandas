import pandas as pd
import numpy
from urllib.parse import urlparse

# Series
print('Series:')
series_test = pd.Series([100, 200, 300])
print(series_test)
print('- - - - - - - - - - - - ')

series_test2 = pd.Series({1999: 48,
                          2000: 65,
                          2001: 89})
print(series_test2)
print('- - - - - - - - - - - - ')

# DataFrames
frame_test = pd.DataFrame({1999: [74, 38, 39],
                           2000: [34, 32, 32],
                           2011: [23, 39, 23]})
print('DataFrames:')
print(frame_test)
print('- - - - - - - - - - - - ')

frame_test2 = pd.DataFrame([[74, 38, 39],
                           [34, 32, 32],
                           [23, 39, 23]])
print(frame_test2)
print('- - - - - - - - - - - - ')

frame_test3 = pd.DataFrame([[74, 38, 39],
                           [34, 32, 32],
                           [23, 39, 23]], columns=[1999, 2000, 2001])
print(frame_test3)
print('- - - - - - - - - - - - ')

# Read Data
pd.options.display.max_rows = 10
el_universal = pd.read_csv('eluniversal_2020_01_27_articles.csv')
print(el_universal.head())
print(el_universal.tail())
print('- - - - - - - - - - - - ')

# Dictionary like

print(el_universal['title'])
print(el_universal[['title', 'body']])

print('- - - - - - - - - - - - ')

# Numpy like

print(el_universal.iloc[1:10])
print('- - - - - - - - - - - - ')
print(el_universal.iloc[12]['title'])
print('- - - - - - - - - - - - ')
print(el_universal.iloc[:5, 0])
print('- - - - - - - - - - - - ')

print(el_universal.loc[:, 'body':'title'])
print('- - - - - - - - - - - - ')

# Data Wrangling
# 1 Añadir newspaper_uid al DataFrame
el_universal['newspaper_uid'] = 'eluniversal'
print(el_universal)

# 2 Obtener el host
el_universal['host'] = el_universal['url'].apply(lambda url: urlparse(url).netloc)
print(el_universal)

print(el_universal['host'].value_counts())

