import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
file = open('list.txt', 'r').read().split('\n')
for link in file:
        if link == "":
                continue
        url = "https://viewdns.info/reverseip/?host="+link+"&t=1"
        text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(text, 'html.parser')
        narrow = soup.find('table', attrs={'border':'1'})
        domain = narrow.findAll('td', attrs={'align':None})[2:]
        for line in domain:
                print(line.text)


        
    


    
