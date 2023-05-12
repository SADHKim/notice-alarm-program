from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import mail

drive = None
prev_lists = {}

def make_driver():
    # 드라이버 경로
    path = '/usr/bin/geckodriver'

    # 웹 드라이버 설정
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # 브라우저 백그라운드 실행
    options.add_argument('--disable-blink-features=AutomationControlled')
    global driver
    driver = webdriver.Firefox(executable_path=path, options=options)
    
def return_driver():
    global driver
    driver.quit()
    driver = None

def get_posts(site):
    
    try:
        ret = [] # 리턴하는 값 : 새로 추가된 게시글 #
        tmp = [] # 새로 크롤링한 게시글들을 저장하는 리스트 #
        
        name = site['name']
        url = site['url']
        className = site['class']
        path = site['path']
        
        
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, className)))
        
        posts = driver.find_elements(By.XPATH, path)
        
        flag = False
        if name in prev_lists:
            flag = True
        
        for post in posts:
            title = post.get_attribute('innerText').strip()
            tmp.append(title)
            
            if flag is False:
                continue
            
            if not title in prev_lists[name]:
                ret.append(title)
            
        prev_lists[name] = tmp
        print('not errer at', site['name'])
        return ret
    except:
        print('!!!!! errer at', site['name'], '!!!!!')
        mail.send_error_mail(site)
        print('!!!!! sending mail completed !!!!!')
        
        return []
    

def crawling(site):
    
    posts = get_posts(site)
    
    if len(posts) >= 1:
        return ({'name' : site['name'], 'url' : site['url'], 'posts' : posts})
    else:
        return False
