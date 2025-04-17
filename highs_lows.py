import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件之中获取最高气温和日期和最低气温
filename ='sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs=[]
    dates=[]
    lows=[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        low = int(row[3])
        lows.append(low)

    #根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形的格式
plt.title("Daily high temperatures - 2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()