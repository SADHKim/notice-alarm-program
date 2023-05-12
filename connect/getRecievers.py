### get users' mail from database ###
import requests
from conf import SECRET_KEY


### the function returns recievers list(tuple) with database table name as params ###
def get_recievers(websiteName):
    
    
    url = 'http://notice-alarm.com/api/get/recievers?key=' + SECRET_KEY + '&website=' + websiteName
    response = requests.get(url=url)
    
    recievers = response.json()
    
    return recievers['list']