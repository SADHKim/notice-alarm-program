from .checking_websites import crawling, make_driver, return_driver
import mail
import connect


def checking():
    result = []
    
    sites = connect.get_websites()
    make_driver()
    mail.send_start_mail(len(sites))
    print('!!! crawling start !!!')
    
    for site in sites:
        result.append(crawling(site))
    
    return_driver()

    return result