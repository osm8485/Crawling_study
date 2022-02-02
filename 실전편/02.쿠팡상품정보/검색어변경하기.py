import requests
from bs4 import BeautifulSoup
import pyautogui
from openpyxl import Workbook

keyword = pyautogui.prompt("검색어를 입력하세요 : ")

wb = Workbook()
ws = wb.create_sheet(keyword)
ws.append(['순위', '브랜드명','상품명','가격','상세페이지링크'])

rank = 1
done = False

for i in range(1,6):
    if done == True:
        break
    else:
        print(i, '번째 페이지 입니다.')
        main_url = f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user&page={i}"

        # 헤더에 User-Agent를 추가하지 않으면 오류가난다(멈춰버림)
        response = requests.get(main_url, headers={'User-Agent' : 'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        links = soup.select("a.search-product-link")

        for link in links:
            # 광고상품제거
            if len(link.select('span.ad-badge-text')) > 0 :
                print("광고상품입니다.")
                # continue >> 안써도됨!
            else :
                sub_url = "https://www.coupang.com" + link.attrs['href']
                response = requests.get(sub_url, headers={'User-Agent' : 'Mozila/5.0'})
                html = response.text
                soup_sub = BeautifulSoup(html, 'html.parser')
                # 브랜드명은 있을수도 있고, 없을 수도 있다.
                ## 중고상품일 때는 태그가 달라진다
                # try -except로 예외처리를 해준다
                try:
                    brand_name = soup_sub.select_one('a.prod-brand-name').text
                except:
                    brand_name = ""
                product_name = soup_sub.select_one('h2.prod-buy-header__title').text
                price = soup_sub.select_one('span.total-price > strong').text
                print(rank, brand_name, product_name, price)
                ws.append([rank, brand_name, product_name, price, sub_url])
                rank += 1
                if rank > 100 :
                    done = True
                    break

wb.save(f'실전편/02.쿠팡상품정보/{keyword}_result.xlsx')