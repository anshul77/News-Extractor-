# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 20:14:06 2018

@author: anshul
"""
import requests
import sys
from bs4 import BeautifulSoup
from newspaper import Article

r = requests.get('https://timesofindia.indiatimes.com/business') 
print(r)
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
links = soup.find('div',attrs={'class':'top-newslist'})

#for i in enumerate(link):
#extract=link.find_all('span',class_='w_tle')
#print(extract)
f=open("summ.txt","w+")
lin=links.find_all('a')
link=[]
for i in lin:
    url="https://timesofindia.indiatimes.com/"+i.attrs['href']
    print(url)
    toi_article = Article(url) 

    toi_article.download()

    toi_article.parse()

    toi_article.nlp()

    print("Article's Summary:")
    f.write(toi_article.title)
    f.write('\n\n')
    f.write(toi_article.summary)
    f.write('\n\n\n\n')
