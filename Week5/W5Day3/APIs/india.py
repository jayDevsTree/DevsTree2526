import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('C:/Users/jaykp/Desktop/Devstree Task/Week5/W5Day3/allAPI.env')

INDIA_API = os.getenv('COUNTRY')

def get_news():
    url = f"{INDIA_API}"
    res = requests.get(url)
    data = res.json()
    
  
    
get_news()