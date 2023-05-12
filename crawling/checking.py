from .checking_websites import crawling, make_driver, return_driver, get_prev_list, store_prev_list
import mail
import connect


def checking():
    result = []
    
    sites = connect.get_websites()
    make_driver()
    get_prev_list()
    mail.send_start_mail(len(sites))
    
    for site in sites:
        result.append(crawling(site))
    
    return_driver()
    store_prev_list()

    return result