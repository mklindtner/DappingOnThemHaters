import requests
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


checkRequestUrl('https://api.github.com')
checkRequestUrl('https://NotRealAtlltFUck.com')
checkRequestUrl('I AM NOT FUCKIGN REAL ? ')




#make dict for all https:

#go through 1 page and find all links
#use selenium to go to next page





