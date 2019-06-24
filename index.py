# import core dependencies

from dotenv import load_dotenv
import os
import smtplib 
import requests
import json


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# configure environment 

import portfolio
import message

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
msg = MIMEMultipart('alternative')
msg['Subject']='Daily Financials'
html = message.email(closing_price,change)


message = MIMEText(html,'html')
msg.attach(message)

s.sendmail(str(user), 'michaelscottfox1@gmail.com', msg.as_string())
s.quit()
