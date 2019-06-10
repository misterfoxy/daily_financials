import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup
import bs4

import json

response = requests.get("https://cloud.iexapis.com/stable/stock/SPY/quote?token=pk_66584401576d4f9d88c4e03e082f6375", timeout=240)
data = response.json()
print('Close: ' + str(data['close']))
print('One Day Change: '+ str(data['change']))
