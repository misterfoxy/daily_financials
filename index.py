from dotenv import load_dotenv
load_dotenv()

import os
api_key = os.getenv('APIKEY')
user = os.getenv('GMAIL_USER')
passkey = os.getenv('GMAIL_PASS')

import smtplib 
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(str(user),str(passkey))

import requests
import json

import portfolio
stock_arr = portfolio.stock_arr()
stocks = portfolio.stocks()

response = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?token="+str(api_key)+"&symbols="+str(stocks)+"&types=quote,news,chart&range=1m&last=5", timeout=260)
data = response.json()

closing_price = str(data[stock_arr[0]]['quote']['close'])
change = str(data[stock_arr[0]]['quote']['change'])

message = 'Closing price of $' + closing_price + ' for '+ stock_arr[0] + ' today, a change of ' + change + '!'

s.sendmail(str(user), 'michaelscottfox1@gmail.com', message)
s.quit()
