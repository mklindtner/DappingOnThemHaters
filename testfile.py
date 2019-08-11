#from crawler import checkRequestUrl
test_address = "https://www.promocasumo.com/tracking/5d0b4354a400a827829a7e1c?src=5be00d3c320afd0b38bd94de&amp;s1=&amp;s2=&amp;s3=&amp;s4=&amp;s5=&amp;k=5d0b45bda400a827829a7f8c"
import re
import requests

#print(checkRequestUrl(test_address))
link = "\"https://www.plusserviceonline.com/marketing/endpage-offers?page=2\""
print(link[1:-1]) #get first element and remove first " and last ""
print(requests.get(test_address).status_code)