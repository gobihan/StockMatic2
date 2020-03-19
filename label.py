import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import csv
 
parse_dates = ['Date']
with open('data.csv', 'rb') as csvfile:

    data = pd.read_csv("data.csv", index_col="Date", parse_dates=parse_dates) 

# print(data['Close'])

# plt.plot(data['Close'])
# plt.title('Daily Price of MSFT')
# plt.xlabel('Date')
# plt.ylabel('Price');


# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# returns a value representing how much the stock has changed for that day
def getSdChangeInPrice(close_prices, lookback = 20):
    daily_vol = close_prices.index.searchsorted(close_prices.index - pd.Timedelta(days=1))
    daily_vol = daily_vol[daily_vol>0]
    daily_vol = pd.Series(data=close_prices.index[daily_vol - 1], index=close_prices.index[close_prices.shape[0]-daily_vol.shape[0]:])

    try:
        daily_vol = (close_prices.loc[daily_vol.index] / close_prices.loc[daily_vol.values].values-1) # daily returns
    except Exception as e:
        print('error: {}\nplease confirm no duplicate indices'.format(type(e).__name__, e))

    daily_vol = daily_vol.ewm(span=lookback).std()

    # print(daily_vol)

    return daily_vol.iloc[1:]

def TripleBarrierMethod(data):

    upper_lower_multipliers=[2,2] # how risky you want this to be, the lower it is the more riskier (less holding)

    t_final = 10 # it is how many days ahead to check if the price move significantly, size of window
    close_prices = data['Close']
    highs = data['High']
    lows = data['Low']
    daily_vol = getSdChangeInPrice(close_prices) # how much it has changed for each day

    # print ("{}, {}, {}, {}".format(type(close_prices), highs, lows, daily_vol))

    # print(type(daily_vol))
    out = pd.DataFrame(index = daily_vol.index) # creating a dataframe, with dates as index
    out['Open'] = data['Open']
    out['High'] = highs
    out['Low'] = lows
    out['Close'] = close_prices
    out['Volume'] = data['Volume']
    out['Daily_Vol'] = daily_vol

    # out.at["2010-02-08 00:00:00", "Security"] = 1

    # print(out)

    for day, sdChangeInPrice in daily_vol.iteritems():
        # print(day, vol)

        days_passed = len(daily_vol[daily_vol.index[0] : day])
        # print(days_passed)

        if (days_passed + t_final < len(daily_vol.index) and t_final != 0): # checks if enough values for window to be size 10
            vert_barrier = daily_vol.index[days_passed + t_final] # the vertical barrier is today plus window size.
            # if today is the 10th March, then the vertical barrier is the 20th March
        else:
            vert_barrier = np.nan

        # set the top barrier to current price plus how much the price changed in last 20 days
        # it is the value at which if the price reaches in the future, it would be considered a buy today.
        if upper_lower_multipliers[0] > 0:
            top_barrier = close_prices[day] + close_prices[day] * sdChangeInPrice * upper_lower_multipliers[0]  
        else:
            # top_barrier = pd.Series(index=close_prices.index) # NaNs
            top_barrier = np.nan # NaNs

        # set the bottom barrier to current price minuses how much the price changed in last 20 days
        # it is the value at which if the price reaches in the future, it would be a considered a sell today.
        if upper_lower_multipliers[1] > 0:
            bot_barrier = close_prices[day] - close_prices[day] * sdChangeInPrice * upper_lower_multipliers[1] 
            # 450       =  500(price today) -  500(price today) *     0.1         *  1
            # if the price hits 450(bottom barrier) then within the next 10 days(t_final) we consider it a sale today at price 500.
        else:
            # bot_barrier = pd.Series(index=close_prices.index) # NaNs
            bot_barrier = np.nan # NaNs

        # print(top_barrier, bot_barrier)

        breakthrough_date = vert_barrier # if the price doesn't go up or down, then the breakthrough date is set to the vertical barrier, which is the date in 10 days.
            
        # For t_final days after current date (or remaining days in time_frame, whichever ends first)
        # for the next 10 days
        for future_date in daily_vol.index[days_passed : min(days_passed + t_final, len(daily_vol.index))]:
            # print(future_date)
            # if the high of these 10 days is higher than the barrier, then the date this happens becomes our breakthrough date.
            if ((highs[future_date] >= top_barrier or 
                     close_prices[future_date] >= top_barrier and
                     top_barrier != 0)):
                        out.at[day, "Buy"] = 1
                        out.at[day, "Sell"] = 0
                        breakthrough_date = future_date
                        break
            elif (lows[future_date] <= bot_barrier or
                      close_prices[future_date] <= bot_barrier and 
                      bot_barrier != 0):
                    out.at[day, "Buy"] = 0
                    out.at[day, "Sell"] = 1
                    breakthrough_date = future_date
                    break

        # if it not a buy or a sell, here we calculate the value in between
        if (breakthrough_date == vert_barrier):
            # Initial and final prices for Security on timeframe (purchase, breakthrough)
            price_initial = close_prices[day]
            price_final   = close_prices[breakthrough_date]

            if price_final > top_barrier:
                out.at[day, "Buy"] = 1
                out.at[day, "Sell"] = 0
            elif price_final < bot_barrier:
                out.at[day, "Buy"] = 0
                out.at[day, "Sell"] = 1
            else:
                # out.at[day, "Security"] = max([(price_final - price_initial) / (top_barrier - price_initial),
                #                              (price_final - price_initial) / (price_initial - bot_barrier)], key=abs)
                out.at[day, "Buy"] = 0
                out.at[day, "Sell"] = 0
            # print(price_initial, price_final)

    # print(highs["2018-05-04 00:00:00"])
    # print(highs["2018-05-04 00:00:00"])
    return out[:-1]
    
out = TripleBarrierMethod(data)
out = out.dropna()
# print(get_daily_vol(data["Close"]))
# daily_vol = get_daily_vol(data["Close"]) 
# print(daily_vol)
print(out)

# plt.plot(out['Buy'],'bo')
# plt.show()

# trainingData = pd.DataFrame(columns=data.columns)
# testingData = pd.DataFrame(columns=data.columns)

# for i in range(len(out)):
#     if(i < len(out)*0.8):
#         # print(out.iloc[i])
#         trainingData = trainingData.append(out.iloc[i])
#     else:
#         testingData = testingData.append(out.iloc[i])

# trainingData.to_csv(r'trainingData.csv')
# testingData.to_csv(r'testingData.csv')
out.to_csv(r'data5.csv')
# labelled data should be of the form 
# date, close price, high, volume, change in SD etc
'''
We now have labelled data for each date, whether we should buy, sell or hold
Remember, lower and higher mutipliers determine riskiness
Consider, time intervals
Create a model using tensorflow of this labelled data, and test it. Train and test
We have buy and sell, and we now need take profit and stop loss.
Our labelled data for buy and sell is now our unlabelled data for taking profit and stock loss.
By how much do we want to buy and sell, this what we have to label, using meta labelling.
Find articles on meta labelling, and send them to the big boi.
Find some code for this labelling.
Put that through a TensorFlow, potentially a Regression model.
'''