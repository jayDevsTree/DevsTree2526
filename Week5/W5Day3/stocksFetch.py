import requests
import json

url = 'https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata'


def fetch_stocks():
   
    response = requests.get(url)
    
    data = response.json()
    
    if data['statusCode']== 200 and data['success'] and data['data']:
        print(data['message'])
        print()
        stocks = data['data']['data']
        for i in range(len(stocks)):
            symbol = stocks[i]['Symbol']
            name = stocks[i]['Name']
            market_cap = stocks[i]['MarketCap']
            current_price = stocks[i]['CurrentPrice']
            print('Symbol:',symbol)
            print('Name:',name)
            print('MarketCap:',market_cap)
            print('CurrentPrice:',current_price)
            print("-----------------")
            
        return data,stocks
    else:
        raise Exception("No data found")
    
def write_stocks(stocks):
    with open('stocks.json','w') as stock_file:
        json.dump(stocks,stock_file,indent=4)
    
def read_stocks():
    with open('stocks.json','r') as stock_file:
        data = json.load(stock_file)
        print(data)
        
        
        
#this is the main function

if __name__ == "__main__":
    allData,stocks = fetch_stocks()
    write_stocks(allData)
    # read_stocks()
    