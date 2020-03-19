import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import talib as ta
# Machine learning
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("data5.csv")
df_train = data[:2000]
df_test = data[2000:]

train_date = df_train.pop("Date")
test_date = df_test.pop("Date")

scaler = MinMaxScaler()
# df_train.pop("Volume")
# df_test.pop("Volume")

df_train['S_10'] = df_train['Close'].rolling(window=10).mean()
df_train['Corr'] = df_train['Close'].rolling(window=10).corr(df_train['S_10'])
df_train['RSI'] = ta.RSI(np.array(df_train['Close']), timeperiod=10)
df_train['Open-Close'] = df_train['Open'] - df_train['Close'].shift(1)
df_train['Open-Open'] = df_train['Open'] - df_train['Open'].shift(1)
# df_train['Open']= df_train['Open']/df_train['Open'].max()
# df_train['High']= df_train['High']/df_train['High'].max()
# df_train['Low']= df_train['Low']/df_train['Low'].max()
# df_train['Close']= df_train['Close']/df_train['Close'].max()
df_train['Volume']= df_train['Volume']/df_train['Volume'].max()

df_train = df_train.dropna()

df_test['S_10'] = df_test['Close'].rolling(window=10).mean()
df_test['Corr'] = df_test['Close'].rolling(window=10).corr(df_test['S_10'])
df_test['RSI'] = ta.RSI(np.array(df_test['Close']), timeperiod = 10)
df_test['Open-Close'] = df_test['Open'] - df_test['Close'].shift(1)
df_test['Open-Open'] = df_test['Open'] - df_test['Open'].shift(1)
# df_test['Open']= df_test['Open']/df_test['Open'].max()
# df_test['High']= df_test['High']/df_test['High'].max()
# df_test['Low']= df_test['Low']/df_test['Low'].max()
# df_test['Close']= df_test['Close']/df_test['Close'].max()
df_test['Volume']= df_test['Volume']/df_test['Volume'].max()
df_test = df_test.dropna()
# print(df_train.shape, df_test.shape)
# print(df_train.dtypes)
# print(df_train)


df_train_label = df_train.pop('Buy')
df_test_label = df_test.pop('Buy')

df_train_label1 = df_train.pop('Sell')
df_test_label1 = df_test.pop('Sell')

# data_training = scaler.fit_transform(df_train)
# data_testing = scaler.transform(df_test)

data_training = df_train
data_testing = df_test

model = LogisticRegression()
model = model.fit(data_training,df_train_label)

probability = model.predict_proba(data_testing)
# df_test['Probability'] = probability

predicted = model.predict(data_testing)
# print(type(predicted))

actual = df_test_label.to_numpy()

correct = []

for i in range(len(predicted)):
    if predicted[i] == actual[i]:
        correct.append(predicted[i])
    else:
        correct.append(0)
    
    print(predicted[i], actual[i], probability[i][1])

# print (metrics.confusion_matrix(actual, predicted))

# print (metrics.classification_report(actual, predicted))

print ("Accuracy",model.score(df_test,df_test_label))

panda_probability = pd.DataFrame(probability, index=df_test.index)
panda_predicted = pd.DataFrame(predicted, index=df_test.index)
buy = pd.DataFrame(correct, index=df_test.index)

# print("Probability", list(panda_probability.columns))
# print("df_test", len(df_test))
# print(panda_probability[1])
df_test['Probability'] = panda_probability[1]
# df_test['Predicted'] = panda_predicted
# df_test["Label"] = df_test_label
df_test["Date"] = test_date
df_test["Buy"] = buy

print(df_test)

df_test.to_csv(r'data6.csv', index=None)
# print(predicted)
# print(actual)
