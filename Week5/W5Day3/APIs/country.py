import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('C:/Users/jaykp/Desktop/Devstree Task/Week5/W5Day3/allAPI.env')

COUNTRY_API = os.getenv('COUNTRY_API')

def get_news():
    url = f"{COUNTRY_API}"
    res = requests.get(url)
    data = res.json()
    
    
get_news()