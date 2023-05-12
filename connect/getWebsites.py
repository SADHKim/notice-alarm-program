import requests

def get_websites():
    url = 'http://notice-alarm.com/api/get/websites'
    response = requests.get(url=url)
    
    websites = response.json()
    
    return websites