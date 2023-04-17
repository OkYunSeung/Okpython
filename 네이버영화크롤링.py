import bs4
import requests
import pandas as pd

real_answer_list = []
score_list = []

for page_no in range(1, 101):

    page_url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=223800&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page={page_no}"    

    source = requests.get(page_url).text
    source = bs4.BeautifulSoup(source)

    answer_list = []
    for i in range(0, 10):
        answer = source.find_all("span", id = f"_filtered_ment_{i}")
        answer_list.append(answer)

    for answers in answer_list:
        real_answer_list.append(answers[0].text)
    len(real_answer_list)

    scores = source.find_all("div", class_ = "star_score")

    for score in scores:
        score_list.append(score.text)
        
df = pd.DataFrame({"score" : score_list, "answer" : real_answer_list})

df.to_excel("네이버 영화 슬램덩크 댓글 크롤링.xlsx", index=False)