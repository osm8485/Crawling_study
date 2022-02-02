import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\o9707\Desktop\대학교\inflearn\crawling\기본편\02.네이버_주식현재가\참가자_data.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택(기본시트)

codes = [
    '005930',
    '000660',
    '035720',
]

row = 4
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(f"code : {code}, price : {price}")
    ws[f'A{row}'] = int(price)
    row +=1

wb.save(fpath)