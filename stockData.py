import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

# from pyspark import SparkContext
# sc = SparkContext()

msft = yf.Ticker("msft")
# print(msft)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
info = msft.info['sector']

print(info)

"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'sector': 'Technology'
 'symbol': 'MSFT'
}
"""

# print(info)

# get historical market data
data = msft.history(period='4m', interval='2m')
"""
returns:
              Open    High    Low    Close      Volume  Dividends  Splits
Date
1986-03-13    0.06    0.07    0.06    0.07  1031788800        0.0     0.0
1986-03-14    0.07    0.07    0.07    0.07   308160000        0.0     0.0
...
2019-04-15  120.94  121.58  120.57  121.05    15792600        0.0     0.0
2019-04-16  121.64  121.65  120.10  120.77    14059700        0.0     0.0
"""

# print(data)

# show actions (dividends, splits)
msft.actions
"""
returns:
            Dividends  Splits
Date
1987-09-21       0.00     2.0
1990-04-16       0.00     2.0
...
2018-11-14       0.46     0.0
2019-02-20       0.46     0.0
"""

# show dividends
msft.dividends
"""
returns:
Date
2003-02-19    0.08
2003-10-15    0.16
...
2018-11-14    0.46
2019-02-20    0.46
"""

# show splits
msft.splits
"""
returns:
Date
1987-09-21    2.0
1990-04-16    2.0
...
1999-03-29    2.0
2003-02-18    2.0
"""

# data2 = yf.download("AAPL", start="2000-01-01", end="2020-01-01")
# print(data2)

# def label(data):
#     windowSize = 11
#     counter = 0
#     results = []

#     while counter < len(data):
#         counter+=1
#         results.append(0)
#         if counter > windowSize:
#             windowBeginIndex = counter - windowSize
#             windowEndIndex = windowBeginIndex + windowSize - 1 
#             windowMiddleIndex = (windowBeginIndex + windowEndIndex) / 2 
#             min = 100000000000
#             max = 0
#             minIndex = 0
#             maxIndex = 0
#             for i in range(windowBeginIndex, windowEndIndex):
#                 number = data.iloc[i]['Close']
#                 if number < min:
#                     min = number
#                     minIndex = i
#                 if number > max:
#                     max = number
#                     maxIndex = i
#             if maxIndex == windowMiddleIndex:
#                 # data.iloc[i]['Result'] = "SELL"
#                 results[counter-1]=-1
#             elif minIndex == windowMiddleIndex:
#                 # data.iloc[i]['Result'] = "BUY"
#                 results[counter-1]=1
#                 # print("69")
#             # else:
#                 # results[counter]="yo"
#             #     # data.iloc[i]['Result'] = "HOLD"
#             #     results.append("HOLD")

#     data['Result'] = results
#     return results
#     # print(results)
#     # print("{},{}".format(len(data), len(results)))
    
    
# # x = map(label, data)

# # print(x)

# # data.set_index("Result", inplace = True) 

# labels = label(data)
# print(data)
# sample = open('data.txt', 'a+')
# sample2 = open('labels.txt', 'a+')
data.drop(["Dividends","Stock Splits"], axis = 1, inplace = True) 
# # print(data.columns)
# # print(data.to_numpy())
# # counter = 0

# # values = data.to_numpy()

# trainingData = pd.DataFrame(columns=data.columns)
# testingData = pd.DataFrame(columns=data.columns)

# lastOnTrainingData = 0

# for i in range(len(data)):
#     if(i < len(data)*0.8):
#         trainingData = trainingData.append(data.iloc[i])
#     else:
#         testingData = testingData.append(data.iloc[i])

# print(lastOnTrainingData)

# for i in range(len(values)):
#     print(values[i], file = sample)
#     print(values[i])

# for i in range(len(labels)):
#     print(labels[i], file = sample2)

# trainingData.to_csv(r'training_data.csv')
# testingData.to_csv(r'testing_data.csv')
# for key in data:
#     print(data[key])
print(data)
# for data_point in data.index:
#     print(data.loc[data_point, "Open"])
# data.to_csv(r'data.csv')


# print(values)


# for row in data.iterrows():
#     # counter+=counter+1
#     print(row, file = sample )
# print(data, file=sample)

# print(data.values())
# for i in range(len(data)):
#     print(data[i])

# print(counter)

# for i in range(1,10):
#     print(data)



# data.Close.plot()

# close_px = data.Close
# mavg = close_px.rolling(window=100).mean()

# # print(mavg)

# mavg.plot()
# plt.show()