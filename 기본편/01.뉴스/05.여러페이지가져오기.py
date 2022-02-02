import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>")
lastpage = int(pyautogui.prompt("마지막 페이지 번호를 입력하세요>>>"))

pageNum = 1
 
for i in range(1, lastpage*10, 10):
    print(f"===================={pageNum}페이지 입니다 =========================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    for link in links:
        title = link.text # 태그 안에 텍스트요소를 가져온다
        url = link.attrs['href'] # href의 속성값을 가져온다
        print(title, url)
    pageNum += 1
    
