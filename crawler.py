import requests
urls_response = {}

def checkRequestUrl(url):
    request = requests.get(url)    
    try:
        urls_response[url] = request.status_code
        # urls_response[url] = 404
        print(urls_response)
    except:
        urls_response[url] = 404


checkRequestUrl('https://api.github.com')
checkRequestUrl('https://NotRealAtlltFUck.com')




#make dict for all https:
#use regular expression to find http://... 
#go through 1 page and find all links
#use selenium to go to next page


