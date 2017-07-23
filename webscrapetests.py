from bs4 import BeautifulSoup
import urllib.request
import html5lib
import time

source = urllib.request.urlopen('https://playoverwatch.com/en-us/blog/').read()
soup = BeautifulSoup(source, 'html5lib')

latest_article = soup.find(class_='link-title')['title']

def new_article_check():
    check_source = urllib.request.urlopen('https://playoverwatch.com/en-us/blog/').read()
    check_soup = BeautifulSoup(check_source, 'html5lib')
    check_article = check_soup.find(class_='link-title')['title']
    if latest_article == check_article:
        print("No New Article")
    else:
        print("New Article, actions will go here")
        print(latest_article['title'])
    time.sleep(20)

while True:
    new_article_check()
