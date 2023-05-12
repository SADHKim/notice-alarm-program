import requests

def get_websites():
    url = 'http://notice-alarm.com/api/get/webistes'
    response = requests.get(url=url)
    
    websites = response.json()
    
    return websites