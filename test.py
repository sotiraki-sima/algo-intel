import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')
#style.use('fivethirtyeight')

start = dt.datetime.now() - timedelta(days=2*365) #dt.datetime(20.019, 1, 1, 1)
end = dt.datetime.now()

df = web.DataReader("PFE", 'yahoo', start, end)
print(df.head(10))



output1 = open("output1.csv", "w")
output1.write("open_dif\tclose_dif\tstatus\n")

close_previous_day = 0.0

long_on_negatives = [0.0,0.0]
short_on_negatives = [0.0,0.0]
long_on_positives = [0.0,0.0]
short_on_positives = [0.0,0.0]

long_wins = 0.0
short_wins = 0.0

for i in range(1,len(df['Close'])):
    position = "NONE"

    if (df['Close'][i] - df['Open'][i]) > 0.0:
        position = "LONG"
        long_wins += float(df['Close'][i] - df['Open'][i])
        if float(df['Open'][i] - df['Close'][i-1]) < 0.0:
            long_on_negatives[0] += 1
        elif float(df['Open'][i] - df['Close'][i-1]) > 0.0:
            long_on_positives[0] += 1

    elif (df['Close'][i] - df['Open'][i]) < 0.0:
        position = "SHORT"
        short_wins += -1*float(df['Close'][i] - df['Open'][i])
        if float(df['Open'][i] - df['Close'][i-1]) < 0.0:
            short_on_negatives[0] += 1
        elif float(df['Open'][i] - df['Close'][i-1]) > 0.0:
            short_on_positives[0] += 1


    output1.write(
        str(df['Open'][i] - df['Close'][i-1])+
        "\t" +
        str(df['Close'][i] - df['Open'][i])+
        "\t" + 
        position +
        "\n")

print("long_on_negatives " + str(long_on_negatives[0]/(len(df['Close']))*100) + ", total: " + str(long_wins))
print("long_on_positives " + str(long_on_positives[0]/(len(df['Close']))*100)+ ", total: " + str(long_wins))
print("short_on_negatives " + str(short_on_negatives[0]/(len(df['Close']))*100) + ", total: " + str(short_wins))
print("short_on_positives " + str(short_on_positives[0]/(len(df['Close']))*100) + ", total: " + str(short_wins))

output1.close()

#df['Adj Close'].plot()
#plt.legend()
#plt.show()

