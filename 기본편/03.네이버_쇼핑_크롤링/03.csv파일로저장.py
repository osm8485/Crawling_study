from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com/')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지 기다림
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2) # 2초 멈춤

search = browser.find_element_by_css_selector('input.co_srh_input._input')

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER) # 엔터 치는 명령어

before_h = browser.execute_script("return window.scrollY") #execute_script = 자바스크립트 명령어 실행

while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1) 
    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h 
items = browser.find_elements_by_css_selector('.basicList_item__2XT81')

# 파일 생성
f = open(r'C:\Users\o9707\Desktop\대학교\inflearn\crawling\기본편\03.네이버_쇼핑_크롤링\data.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.price_num__2WUXn').text
    except:
        price = '판매중단'
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name, price, link)
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])

# 파일 닫기
f.close()
