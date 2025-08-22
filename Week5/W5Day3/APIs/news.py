import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('C:/Users/jaykp/Desktop/Devstree Task/Week5/W5Day3/allAPI.env')

NEWS_API = os.getenv('NEWS_API')

def get_news():
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-07-21&sortBy=publishedAt&apiKey={NEWS_API}"
    res = requests.get(url)
    data = res.json()
  
    
get_news()