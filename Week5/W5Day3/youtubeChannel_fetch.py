import requests

def fetch_youtube_Channel():
    
    url = 'https://api.freeapi.app/api/v1/public/youtube/channel'
    
    result = requests.get(url)
    
    allData = result.json()
    
    if allData['success'] and allData['data']:
        print(allData['message'])
        id = allData['data']['info']['id']
        channel_owner_photo_url = allData['data']['info']['snippet']['thumbnails']['high']['url']
        width_photo = allData['data']['info']['snippet']['thumbnails']['high']['width']
        print(width_photo)
        print(channel_owner_photo_url)
        print(id)
    else:
        print("request Not found!")
        
    
    
    
fetch_youtube_Channel()