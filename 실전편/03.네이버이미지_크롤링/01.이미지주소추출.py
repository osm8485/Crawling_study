from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC%EC%A7%80%EC%88%98'
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)
time.sleep(1)

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

# 이미지 태그 추출
imgs = browser.find_elements_by_css_selector("._image._listImage")

for i, img in enumerate(imgs, 1):
    # 각 이미지 태그의 주소
    img_src = img.get_attribute('src')
    print(i, img)