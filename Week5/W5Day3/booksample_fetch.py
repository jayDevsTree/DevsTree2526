import requests

def book_fetch():
    
    url = 'https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech'
    
    response = requests.get(url)
    
    allData = response.json()
    
    if allData['success'] and allData['data']:
        print(allData['message'])
        prev_page = allData['data']['previousPage']
        print(prev_page)
        print(allData['data']['data'][0]['id']) # output: 2
        print(allData['data']['data'][2]['volumeInfo']['authors'][0]) # Matt Frisbie
    else:
        raise Exception("Not Found!")
    

if __name__ == '__main__':
 
    book_fetch()

