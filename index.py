import numpy as np
import pandas as pd

from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv('APIKEY')

import requests
from bs4 import BeautifulSoup
import bs4

import json

response = requests.get("https://cloud.iexapis.com/stable/stock/SPY/quote?token=" + str(api_key) + "", timeout=240)
data = response.json()
print('Close: ' + str(data['close']))
print('One Day Change: '+ str(data['change']))
