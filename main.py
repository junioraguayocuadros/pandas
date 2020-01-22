import pandas as pd

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

