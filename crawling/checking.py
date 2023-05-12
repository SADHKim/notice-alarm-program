from .checking_websites import crawling, make_driver, return_driver
import mail
import http


def checking():
    result = []
    
    sites = http.get_websites()
    make_driver()
    mail.send_start_mail(len(sites))
    
    for site in sites:
        result.append(crawling(site))
    
    return_driver()

    return result