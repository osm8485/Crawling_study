import requests
from bs4 import BeautifulSoup

# url에서 한글은 인코딩되어서 표시됨
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
# print(links) >>> soup.select에서 전체태그를 리스트 형태로 반환

for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져온다
    url = link.attrs['href'] # href의 속성값을 가져온다
    print(title, url)

