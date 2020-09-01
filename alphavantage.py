import requests
import os
import matplotlib.pyplot as plt
from matplotlib import style

url = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=GBP&to_symbol=EUR&interval=15min&outputsize=compact&apikey=" + os.getenv("alpha_key")
url = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=EUR&apikey=" + os.getenv("alpha_key")
print(url)
response = requests.get(url)
response_json = response.json()

data_key = ""
for key in response_json:
    if key != "Meta Data":
        data_key = key
        break

x_axis = []
y_axis = []

cnt_max = 30
for key in response_json[data_key]:
    cnt_max -= 1
    if cnt_max == 0:
        break
    
    
    clean_key = key.split("-")[2] + "-" + key.split("-")[1] #2020-08-31 22:00:00
    x_axis.insert(0, clean_key)
    y_axis.insert(0, float(response_json[data_key][key]["4. close"]))
    
    #print(x_axis)
    #print(y_axis)




plt.plot(x_axis, y_axis)
plt.ylabel('GBP/EUR')
plt.ylabel('Sexy Vanucha!')

plt.show()