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

# browser.find_element_by_css_selector('a.co_srh_btn._search').click() 으로 직접 검색버튼 눌러도 된다.

