import numpy as np
import pandas as pd

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
from bs4 import BeautifulSoup
import bs4

import json

response = requests.get("https://cloud.iexapis.com/stable/stock/SPY/quote?token=" + str(api_key) + "", timeout=240)
data = response.json()
print('Close: ' + str(data['close']))
print('One Day Change: '+ str(data['change']))


message = 'Closing price of $' + str(data['close']) + ' for the SPY index today, a change of ' + str(data['change']) + '!'

s.sendmail(str(user), 'michaelscottfox1@gmail.com', message)

s.quit()

