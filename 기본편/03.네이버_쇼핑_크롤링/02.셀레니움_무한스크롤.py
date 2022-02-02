from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('./chromedriver')
# 웹사이트 열기
browser.get('https://www.naver.com/')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지 기다림
# 쇼핑 메뉴 클릭, click() 사용
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2) # 2초 멈춤
# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER) # 엔터 치는 명령어

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY") #execute_script = 자바스크립트 명령어 실행

# 무한 스크롤 - 반복문
while True:
    # 맨 아래로 스크롤을 내린다. body = 모든 웹사이트에 존재
    # 키보드의 END키 누르면 웹페이지 맨아래로이동
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1) # 스크롤 사이 페이지 로딩시간
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h  # 스크롤 후 높이가 다르면 before_h를 업데이트

items = browser.find_elements_by_css_selector('.basicList_item__2XT81')

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.price_num__2WUXn').text
    except:
        price = '판매중단'
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name, price, link)
