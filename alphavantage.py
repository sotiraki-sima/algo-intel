import requests
import os
import matplotlib.pyplot as plt
from matplotlib import style


def keys_to_array(json_obj):
    arr = []
    for key in json_obj:
        arr.append(key)
    return arr


ML_BACK_TRACK = 5
MAX_EXTRACT = 60

url = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=EUR&apikey=" + os.getenv("alpha_key")
print(url)
response = requests.get(url)
response_json = response.json()

data_key = ""
for key in response_json:
    if key != "Meta Data":
        data_key = key
        break

output2 = open("output2.csv", "w")
output2.write("      DATE     ____-5     ____-4     ____-3     ____-2     ____-1     ____-0     POSITI     ____+1\n")

for i in range(5,-1,-1):
    print(i)

trade_days = keys_to_array(response_json[data_key])

for x in range (1 ,len(trade_days)-ML_BACK_TRACK):
    output2.write(str(trade_days[x]))

    for i in range(ML_BACK_TRACK, -1, -1):
        output2.write("     " + str(response_json[data_key][trade_days[x+i]]["4. close"]))

    output2.write("\n")
    '''
    output2.write(
        str(trade_days[x]) + "     " + 
        str(response_json[data_key][trade_days[x+5]]["4. close"]) + "     " + 
        str(response_json[data_key][trade_days[x+4]]["4. close"]) + "     " + 
        str(response_json[data_key][trade_days[x+3]]["4. close"]) + "     " + 
        str(response_json[data_key][trade_days[x+2]]["4. close"]) + "     " + 
        str(response_json[data_key][trade_days[x+1]]["4. close"]) + "     " + 
        str(response_json[data_key][trade_days[x]]["4. close"]) + "     " + 
        str("SELLXX") + "     " + 
        str(response_json[data_key][trade_days[x-1]]["4. close"]) + "     " + 
        "\n"
    )
    '''

#x_axis = []
#y_axis = []

#cnt_max = MAX_EXTRACT
#for key in response_json[data_key]:
#    cnt_max -= 1
#    if cnt_max <= MAX_EXTRACT:
#        break
    

    #print(key + "     " + str(float(response_json[data_key][key]["4. close"])))

    #for key_cursor in response_json[data_key]:

    #clean_key = key.split("-")[2] + "-" + key.split("-")[1] #2020-08-31 22:00:00
    #x_axis.insert(0, clean_key)
    #y_axis.insert(0, float(response_json[data_key][key]["4. close"]))
    
    #print(x_axis)
    #print(y_axis)


output2.close()


#plt.plot(x_axis, y_axis)
#plt.ylabel('GBP/EUR')

#plt.show()