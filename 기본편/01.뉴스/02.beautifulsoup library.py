import requests
from bs4 import BeautifulSoup

# naver 서버에 대화 시도, get 요청
response = requests.get("https://www.naver.com/")

# naver에서 html 줌 
html = response.text

# BeautifulSoup(html코드, html번역선생님) >>> html 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# 'NM_set_home_btn'라는 id를 갖는 놈 하나 찾아냄, # = id selector
word = soup.select_one('#NM_set_home_btn') 

# print(word) : a태그 전체가 출력됨, .text로 텍스트 요소만 출력
print(word.text)

