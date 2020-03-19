import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
# raw trade data from https://public.bitmex.com/?prefix=data/trade/ 
data = pd.read_csv(‘data/20181127.csv’)
data = data.append(pd.read_csv(‘data/20181128.csv’)) # add a few more days
data = data.append(pd.read_csv(‘data/20181129.csv’))
data = data[data.symbol == ‘XBTUSD’]
# timestamp parsing
data[‘timestamp’] = data.timestamp.map(lambda t: datetime.strptime(t[:-3], “%Y-%m-%dD%H:%M:%S.%f”))