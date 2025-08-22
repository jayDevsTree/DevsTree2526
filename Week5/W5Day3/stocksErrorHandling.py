import requests
import time
import json

URL = 'https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata'

def error_handling_fetch_stocks(max_retry = 3 , delay = 2):
    
    for attempt in range(max_retry):
    
        try:
            response = requests.get(URL, timeout= 5)
            
            if response.status_code == 200:
                allData = response.json()
                
                if allData['statusCode'] == 200 and allData['success'] and allData['data']:
                    print(allData['message'])
                    print()
                    
                    allData_in_stocks = allData['data']['data']
                    for each_stock in allData_in_stocks:
                        symbol = each_stock['Symbol']
                        name = each_stock['Name']
                        marketCap = each_stock['MarketCap']
                        currentPrice = each_stock['CurrentPrice']
                        
                        print('Symbol:',symbol)
                        print('Name:',name)
                        print('MarketCap:',marketCap)
                        print('CurrentPrice:',currentPrice)
                        print('------------------------------')
                    return allData_in_stocks
    
    
            else:
                print(f'Error : {response.raise_for_status()} Retrying...')
                
        except requests.HTTPError as H :
            print(H)
        except requests.RequestException as R:
            print(R)
        except requests.ConnectionError as C :
            print(C)
        except requests.Timeout as T:
            print(T)
        except requests.ReadTimeout as R:
            print(R)
        
        time.sleep(delay)
    
def write_error_handling_file(stocks_in_allData):
    with open ('stocks_ErrorHandling.json','w') as file:
        json.dump(stocks_in_allData,file,indent=4)
        
def read_error_handling_file():
    with open('stocks_ErrorHandling.json', 'r') as file:
        file_data = json.load(file)
        print(file_data)
  # this is main flow      
if __name__ == '__main__':
    allData_in_stocks =error_handling_fetch_stocks(3,2)
    
    if allData_in_stocks:
        write_error_handling_file(allData_in_stocks)
        read_error_handling_file()
    
    
        