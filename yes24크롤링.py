import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from tqdm.notebook import tqdm #진행도를 확인하기 위함
import seaborn as sns

query = "소설"

titles = [] # 책제목
prices = [] # 책 가격
review_counts = [] # 책 리뷰 수
book_grades = [] # 책 평점
sales_index = [] # 판매 지수


driver = Chrome('chromedriver')


for page_no in tqdm(range(1, 11)):
    page_url = f"http://www.yes24.com/Product/Search?domain=ALL&query={query}&page={page_no}"
    driver.get(page_url)

    book = driver.find_element(By.ID, 'goodsListWrap')
    book_item = book.find_elements(By.CLASS_NAME, 'item_info')

    for i in tqdm(range(len(book_item))):
        book_title = book_item[i].find_element(By.CLASS_NAME, 'gd_name')
        titles.append(book_title.text)

        book_num = book_item[i].find_element(By.CLASS_NAME, 'txt_num')
        book_price = book_num.find_element(By.CLASS_NAME, 'yes_b').text.replace(",","") #txt_num class 안에 있는 yes_b class
        prices.append(book_price)


        try:
            book_review = book_item[i].find_element(By.CLASS_NAME, 'txC_blue')
            review_counts.append(book_review.text)

        except:
            review_counts.append(0) # 리뷰가 없는 도서의 경우에 try except 구문을 통해서 리뷰의 수를 0으로 만들어 줌.

        try:
            book_rating_grade = book_item[i].find_element(By.CLASS_NAME, 'rating_grade')
            book_grade = book_rating_grade.find_element(By.CLASS_NAME, 'yes_b')
            book_grades.append(book_grade.text)

        except:
            book_grades.append(0) # 책 평점이 없는 도서의 경우에 try except 구문을 통해서 책 평점을 0으로 만들어 줌.  

        try:
            book_sale_num = book_item[i].find_element(By.CLASS_NAME, 'saleNum').text[5:].replace(",","")
            sales_index.append(book_sale_num)
        
        except:
            sales_index.append(0) # 판매지수가 없는 도서의 경우에 try except 구문을 통해서 판매지수를 0으로 만들어 줌.
            
 
result = pd.DataFrame({"책 제목" : titles,
                      "가격" : prices,
                      "리뷰 수" : review_counts,
                      "책 평점" : book_grades,
                      "판매 지수" : sales_index})

result.to_excel(f"예스24 ({query})검색.xlsx", index=False)

novel = pd.read_excel("./예스24 (소설)검색.xlsx")

sns.histplot(data=novel, x="판매 지수")
sns.lineplot(data=novel, x="판매 지수", y="리뷰 수")
sns.lineplot(data=novel, x="판매 지수", y="책 평점")