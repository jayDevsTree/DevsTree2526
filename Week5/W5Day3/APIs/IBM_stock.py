import requests
import os
import json
import datetime
from dotenv import load_dotenv

def set_news_url():
    load_dotenv('../allAPI.env')
    BASE_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey="
    STOCK_API = os.getenv('STOCK_API')
    
    if not STOCK_API:
        print("ERROR: API key not found in allAPI.env")
        exit()  
    url = f'{BASE_URL}+{STOCK_API}'
    # data = requests.get(url).json()
    # print(data)
    return url

def set_time_stocks():
    now = datetime.datetime.now()
    prev_day = now - datetime.timedelta(days = 1)
    
    def show_user_prev_day():
        if set_am_pm(user_hours) == 'PM':
            
            prev_day_time = datetime.datetime(prev_day.year, prev_day.month, prev_day.day, user_hours, miniutes)
            # print(prev_day_time+ set_am_pm(user_hours))
            return str(prev_day_time)
        else:
            prev_day_time = datetime.datetime(prev_day.year, prev_day.month, prev_day.day, user_hours, miniutes)
            # print(prev_day_time)
            return f'{str(prev_day_time)} {set_am_pm(user_hours)}'
        
    def show_computer_fetch_data():
        prev_day_time = datetime.datetime(prev_day.year, prev_day.month, prev_day.day, comp_hours, miniutes)
        # print(prev_day_time)
        return str(prev_day_time)
        
  
    def hour_set():
        while True:
            fetch_hour = (input("Enter Hour(11-19):"))
            if fetch_hour.lower() == "exit":
                print("Program terminated by user.")
                exit()
            try:
                right_hour = int(fetch_hour)
                    
                
                if right_hour<0 or right_hour>23:
                    print("Invalid hour Re-enter in (11-19),")
                    # return None
                elif right_hour>=0 and right_hour<11 or right_hour>19:
                    print(f"Sorry {right_hour} hour's Data not available!")
                    print("Re-enter in (11-19),")
                    continue
                # elif not right_hour<20 and not right_hour>10:
                #     print(f"Sorry {right_hour}hour Data not available!")
                #     print("Re-enter in (11-19),")
                #     continue
                else:  
                    user_hour = right_hour - 12
                    computer_hour = right_hour
                    if right_hour > 12:
                        return computer_hour, user_hour
                    else:
                        user_hour = right_hour
                        return computer_hour, user_hour
            except ValueError:
                print("Invalid Input re-enter")
                # return None
                continue   
      
    def min_set():
        while True:
            fetch_min =(input("Enter Min:"))
            if fetch_min.lower() == "exit":
                print("Program terminated by user.")
                exit()
            try:
                right_min = int(fetch_min)
                if right_min<0 or right_min>59:
                    print("Invalid min Re-enter in (0-59),")
                    # return None
                else:
                    if right_min % 5 == 0:
                        return right_min
                    else:
                        return right_min - right_min % 5
            except ValueError:
                print("Invalid Input")
                # return None
                continue
            
    def set_am_pm(hour):
        if hour>=12:
            return 'PM'
        else:
            return 'AM'
        
    comp_hours,user_hours = hour_set()
    miniutes = min_set()
          
    if comp_hours == None or miniutes == None:
        print("Invalid Input")
     
    
    # show_prev_day()
    
    return  show_computer_fetch_data(),show_user_prev_day()
    

def fetch_stocks_detail():
    response = requests.get(url)
    data = response.json()
    stocks_various_price_values=data['Time Series (5min)'][setted_time]
    
    if response.status_code == 200:
        info = data['Meta Data']['1. Information']
        company = data['Meta Data']['2. Symbol']
        last_refresh = data['Meta Data']['3. Last Refreshed']
        data_Interval = data['Meta Data']['4. Interval']
        
        open_val = stocks_various_price_values['1. open']
        high_val = stocks_various_price_values['2. high']
        low_val = stocks_various_price_values['3. low']
        close_val = stocks_various_price_values['4. close']
        volume_val = stocks_various_price_values['5. volume']
        
        return{
            'info':info,
            'company':company,
            'last_refresh':last_refresh,
            'data_Interval':data_Interval,
            'open_val':open_val,
            'high_val':high_val,
            'low_val':low_val,
            'close_val':close_val,
            'volume_val':volume_val
        }
    else:
        response.raise_for_status()
        return None
    
def print_info(info):
    print(f'Information: {info["info"]}')
    print(f'Company: {info["company"]}')
    print(f'Data Interval: {info["data_Interval"]}')
    print(f'Last Refresh: {info["last_refresh"]}')
    print()
    print(f'Time: {setted_user_time}')
    print('----------------------------')
    print(f'Company: {info["company"]}')
    print(f'----------------------------')
    print(f'Open Value: {info["open_val"]}')
    print(f'High Value: {info["high_val"]}')
    print(f'Low Value: {info["low_val"]}')
    print(f'Close Value: {info["close_val"]}')
    print(f'Volume Value: {info["volume_val"]}')
    
url =set_news_url()
setted_time,setted_user_time =set_time_stocks()
print_info(fetch_stocks_detail())
        

        
        
    