import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')
#style.use('fivethirtyeight')

start = dt.datetime.now() - timedelta(days=10*365) #dt.datetime(20.019, 1, 1, 1)
end = dt.datetime.now()

#df = web.DataReader("AMZN", 'yahoo', start, end)

#df = web.DataReader("AAPL", 'yahoo', start, end)
#df = web.DataReader("PFE", 'yahoo', start, end)
#df = web.DataReader("GOOG", 'yahoo', start, end)
df = web.DataReader("TLSA", 'yahoo', start, end)
#df = web.DataReader("JPM", 'yahoo', start, end)
#df = web.DataReader("ZM", 'yahoo', start, end)

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

print("Trade cost: " + str((0.001 * df['Close'][0])))
for i in range(1,len(df['Close'])):
    position = "NONE"

    if (df['Close'][i] - df['Open'][i]) > (0.001 * df['Close'][i]):
        position = "LONG"
        long_wins += float(df['Close'][i] - df['Open'][i])
        if float(df['Open'][i] - df['Close'][i-1]) < 0.0:
            long_on_negatives[0] += 1
        elif float(df['Open'][i] - df['Close'][i-1]) > 0.0:
            long_on_positives[0] += 1

    elif (df['Close'][i] - df['Open'][i]) < (0.001 * df['Close'][i]):
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

print("")
print("On Negative goes Long:\t" + str(long_on_negatives[0]/(len(df['Close']))*100) + "\t total: " + str(long_wins) + "\t real total: " + str(long_wins*long_on_negatives[0]/(len(df['Close']))))
print("On Negative goes Short:\t" + str(short_on_negatives[0]/(len(df['Close']))*100) + "\t total: " + str(short_wins) + "\t real total: " + str(short_wins*short_on_negatives[0]/(len(df['Close']))))
print("Long vs Short:\t " + str(long_wins*long_on_negatives[0]/(len(df['Close'])) - short_wins*short_on_negatives[0]/(len(df['Close']))))
print("")
print("On Positive goes Long:\t" + str(long_on_positives[0]/(len(df['Close']))*100)+ "\t total: " + str(long_wins) + "\t real total: " + str(long_wins*long_on_positives[0]/(len(df['Close']))))
print("On Positive goes Short:\t" + str(short_on_positives[0]/(len(df['Close']))*100) + "\t total: " + str(short_wins) + "\t real total: " + str(short_wins*short_on_positives[0]/(len(df['Close']))))
print("Long vs Short:\t " + str(long_wins*long_on_positives[0]/(len(df['Close'])) - short_wins*short_on_positives[0]/(len(df['Close']))))
print("")

print("No big changes: " + str(
            float(100 - 
                long_on_negatives[0]/(len(df['Close']))*100 - 
                long_on_positives[0]/(len(df['Close']))*100 - 
                short_on_negatives[0]/(len(df['Close']))*100 - 
                short_on_positives[0]/(len(df['Close']))*100 )
                )
    )
output1.close()

#df['Adj Close'].plot()
#plt.legend()
#plt.show()

