import requests
from datetime import datetime
import time



ticker = input("please enter company ticker!")
fr_date = input("enter from date in yyyy/mm/dd format : ")
to_date = input("enter to date in yyyy/mm/dd format : ")

fr_dtime = datetime.strptime(fr_date,'%Y/%m/%d')
to_dtime = datetime.strptime(to_date,'%Y/%m/%d')

fr_epoch = time.mktime(fr_dtime.timetuple())
to_epoch = time.mktime(to_dtime.timetuple())
str1= str(fr_epoch)[:-2]
str2= str(to_epoch)[:-2]
print(str1, str2)
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={str1}&period2={str2}&interval=1d&events=history&includeAdjustedClose=true"
# https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=511108200&period2=1722466780&interval=1d&events=history&includeAdjustedClose=true
#magic headers
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content =  requests.get(url, headers=headers).content;

with open('mikrosoft.csv', 'wb') as file :
    file.write(content)