import schedule
import time

import mail
import crawling
import connect


def search_pages():
    # 크롤링의 결과값 저장 (False or websitename, url, posts : list) #
    try:
        checkResult = crawling.checking()
        
        for result in checkResult:
            if result is False:
                continue
            
            # 해당 웹사이트에서 알림을 받는 사람들 추출#
            recievers = connect.get_recievers(result['name'])
            # recievers가 없다면 continue #
            if recievers is False:
                continue
            
            # Notice object 생성, 내용 만들기 #
            script = mail.Script()
            script.make_script(result['posts'], result['url'], result['name'])
            
            # 메일 전송 #
            mail.send_mail(script, recievers)
    except:
        return
        
        
def start():
    schedule.every().day.at('09:00').do(search_pages)
    schedule.every().day.at('15:00').do(search_pages)
    schedule.every().day.at('21:00').do(search_pages)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == '__main__':
    start()