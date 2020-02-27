import requests
from bs4 import BeautifulSoup

def get_news_from_belta():
    #Getting response from url
    URL = 'https://www.belta.by/all_news'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Finding nessesary page section with news
    results = soup.find(id='inner')
    news_list = results.find_all('div', class_='news_item lenta_item')

    # Making dict format : {n:{news_link, news_title, news_text}}
    all_news_dict = {}
    for news in news_list:
        news_dict = {}
        try:
            #Very strange links building on site
            s = news.find_all('a', href=True)
            news_url = s[0]['href'].split('/')
            news_url = news_url[0]+'//'+news_url[2]+s[1]['href']
            # Fill dict with parts of news
            news_dict['news_link'] = news_url
            news_dict['news_title'] = news.find('span', class_='lenta_item_title').text
            news_dict['news_short_text'] = news.find('span', 'lenta_textsmall').text
            #if something is Null 
        except AttributeError:
            continue
        all_news_dict[news_list.index(news)]= news_dict
    return all_news_dict
    
    