import requests
import bs4
import pandas as pd

date_list = []
title_list = []
for page_no in range(1, 183):
    page_url = f"https://www.khu.ac.kr/kor/notice/list.do?page={page_no}&category=UNDERGRADUATE"

    source = requests.get(page_url).text
    source = bs4.BeautifulSoup(source)

    dates = source.find_all("td", class_ = "col04")
    for date in dates:
        date_list.append(date.text)

    titles = source.find_all('p', class_ = "txt06")

    for title in titles:
        title_list.append(title.text)
     

df = pd.DataFrame({"date" : date_list, "title" : title_list})

df.to_excel("경희대학교 학사 제목과 날짜.xlsx", index=False)