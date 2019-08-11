import requests
from selenium import webdriver
import time

urls_response = {}

def checkRequestUrl(url):    
    if("https" in url):
        try:
            request = requests.get(url)    
            urls_response[url] = request.status_code
        except:
            urls_response[url] = 404
        print(urls_response)

    else:
        print("not today! hosie!")


def getHttpsFromWebsite(url):
    browser = webdriver.Firefox(executable_path  = "/home/mikkel/Documents/geckodriver")
    browser.get(url) 
    email = browser.find_element_by_id('email')
    password = browser.find_element_by_id('password')
    email.send_keys('christian@guzzy.dk')
    password.send_keys('hackerhome')

    #submit_button = browser.find_element_
    #submit_button.click()
    time.sleep(10)
    browser.quit()

getHttpsFromWebsite("https://www.plusserviceonline.com/auth/login")

# checkRequestUrl('https://api.github.com')
# checkRequestUrl('https://NotRealAtlltFUck.com')
# checkRequestUrl('I AM NOT FUCKIGN REAL ? ')




#make dict for all https:

#go through 1 page and find all links
#use selenium to go to next page





