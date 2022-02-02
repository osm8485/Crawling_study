from bs4 import BeautifulSoup
import requests
import time

response = requests.get(
    'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC')

html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select('div.info_group') # 뉴스 기사 div 10개 추출

for article in articles:
    links = article.select('a.info') # 리스트
    if len(links) >= 2: # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href를 추출
        response = requests.get(url, headers = {'User-Agent' : 'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # 만약 연예뉴스라면
        if "entertain" in response.url:      ### 그냥 url사용시 리다이렉션으로 NoneType오류 또 발생, response.url로사용!
            title = soup.select_one('.end_tit').text
            content = soup.select_one('#articeBody').text
        else:
            title = soup.select_one('#articleTitle').text
            content = soup.select_one('#articleBodyContents').text
        print("==============링크=============\n", url.strip())
        print("==============제목=============\n", title.strip())
        print("==============본문=============\n", content.strip())

        
    '''     try:
            content = soup.select_one('#articleBodyContents').text
        except:
            content = soup.select_one('#articeBody').text
        print(content)
        time.sleep(0.3) '''


    