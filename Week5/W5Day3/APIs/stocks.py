# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('C:/Users/jaykp/Desktop/Devstree Task/Week5/W5Day3/allAPI.env')

STOCK_API = os.getenv('STOCK_API')

def get_news():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCK_API}"
    res = requests.get(url)
    data = res.json()
    
   
    
    
get_news()