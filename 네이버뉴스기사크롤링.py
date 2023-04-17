import bs4
import requests
import pandas as pd

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)
name_list = []
company_list = []
for page_no in range(1, 12):
    page_url = f"https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=20230210&page={page_no}"

    source = requests.get(page_url, headers=headers).text
    source = bs4.BeautifulSoup(source)


    names = source.find_all('dt', class_ = False)

    
    for name in names:
        name_list.append(name.text)
    name_list = name_list[:-2:]

    companys = source.find_all("span", class_ = "writing")

    

    for company in companys:
        company_list.append(company.text)


df = pd.DataFrame({"company" : company_list, "name" : name_list})

df.to_excel("네이버 뉴스 기사 크롤링.xlsx", index=False)