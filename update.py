from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import connect
import pickle

prev = None
driver = None

def add_pickle(url):
    make_driver()
    get_prev()
    global prev
    
    websites = connect.get_websites()
    for website in websites:
        if website['url'] != url and url != 'all':
            continue
        
        driver.get(website['url'])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, website['class'])))
        
        posts = driver.find_elements(By.XPATH, website['path'])
        
        tmp = []
        for post in posts:
            title = post.get_attribute('innerText').strip()
            tmp.append(title)
            
        prev[website['name']] = tmp
    
    driver.quit()
    save_list()
    
def pop_pickle(name):
    get_prev()
    global prev
    
    prev.pop(name)
    
    save_list()
        
def make_driver():

    # driver options
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # in background
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    
def get_prev():
    with open('/home/notice-alarm-program/crawling/prev.pickle', "rb") as rf:
        global prev
        prev = pickle.load(rf)
    
def save_list():
    with open('/home/notice-alarm-program/crawling/prev.pickle', 'wb') as wf:
        global prev
        print(prev)
        pickle.dump(prev, wf)
        prev = None
        
if __name__ == '__main__':
    divide = input('What will you exec? (pop, add) : ')
    if divide == 'add':
        url = input('input url : ')
        add_pickle(url)
        print('done')
    elif divide == 'pop':
        name = input('input name : ')
        pop_pickle(name)
        print('done')