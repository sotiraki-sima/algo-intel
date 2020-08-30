import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')
#style.use('fivethirtyeight')

start = dt.datetime.now() - timedelta(days=10) #dt.datetime(2019, 1, 1, 1)
end = dt.datetime.now()

df = web.DataReader("PFE", 'yahoo', start, end)
print(df.head(10))

print(df['Adj Close'][1])


#df['Adj Close'].plot()
#plt.legend()
#plt.show()

