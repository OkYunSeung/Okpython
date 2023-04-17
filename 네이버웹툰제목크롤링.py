import requests
import bs4
import pandas as pd

title_list = []

page_url = "https://comic.naver.com/webtoon/weekday"

source = requests.get(page_url).text
source = bs4.BeautifulSoup(source)

titles = source.find_all("a", class_ = "title")

for title in titles:
    title_list.append(title.text)
    
df = pd.DataFrame({'title' : title_list})

df.to_excel("네이버 웹툰 제목 크롤링.xlsx", index=False)