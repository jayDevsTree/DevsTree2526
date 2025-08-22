import requests
# random user info shows

def fetch_json_data():
    
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
   
    data = response.json()
   
    count = len(data['data'])
    print(count)
    if data["success"] and data['data']:
        userdata = data["data"] 
        gender = userdata["gender"]
        name = userdata['name']['first']
        username = userdata['login']['username']
        
        print(name)
        print(gender)
        print(username)
        print(userdata['email'])
        print("----------------")
    else:
        raise Exception("No data found")
    


def main():
    try:
        fetch_json_data()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()