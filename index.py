# import core dependencies

from dotenv import load_dotenv
import os
import smtplib 
import requests
import json

# configure environment 

import portfolio

load_dotenv()
api_key = os.getenv('APIKEY')
user = os.getenv('GMAIL_USER')
passkey = os.getenv('GMAIL_PASS')

# create transporter
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(str(user),str(passkey))

# read stocks from portfolio file
stock_arr = portfolio.stock_arr()
stocks = portfolio.stocks()

# HTTP GET to iex for quote
response = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?token="+str(api_key)+"&symbols="+str(stocks)+"&types=quote,news,chart&range=1m&last=5", timeout=260)
data = response.json()

# configured currently to pull results just from one stock
closing_price = str(data[stock_arr[0]]['quote']['close'])
change = str(data[stock_arr[0]]['quote']['change'])

# simple no-subject email message of closing price and change
message = 'Closing price of $' + closing_price + ' for '+ stock_arr[0] + ' today, a change of ' + change + '!'

s.sendmail(str(user), 'michaelscottfox1@gmail.com', message)
s.quit()
