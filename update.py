from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import connect
import pickle

posts_list = {}
driver = None

def update_pickle():
    make_driver()
    global posts_list
    
    websites = connect.get_websites()
    for website in websites:
        driver.get(website['url'])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, website['class'])))
        
        posts = driver.find_elements(By.XPATH, website['path'])
        
        tmp = []
        for post in posts:
            tmp.append(post)
            
        posts_list[website['name']] = tmp
        
    save_list()
        


def make_driver():
    # path of firefox
    path = '/usr/bin/geckodriver'

    # driver options
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # in background
    options.add_argument('--disable-blink-features=AutomationControlled')
    global driver
    driver = webdriver.Firefox(executable_path=path, options=options)
    
def save_list():
    with open('/home/notice-alarm-program/crawling/prev.pickle', 'wb') as wf:
        global posts_list
        pickle.dump(posts_list, wf)
        
if __name__ == '__main__':
    update_pickle()