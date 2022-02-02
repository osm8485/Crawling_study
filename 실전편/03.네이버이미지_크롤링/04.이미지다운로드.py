from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request  # 이미지 저장 모듈
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 : ")

if not os.path.exists(f'실전편/03.네이버이미지_크롤링/{keyword}'):   # 해당 폴더의 존재여부를 boolean값으로 출력해줌
    # not True = False : 해당폴더가 기존에 존재하지 않으면 새 폴더를 만든다!
    os.mkdir(f'실전편/03.네이버이미지_크롤링/{keyword}')  

url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query={keyword}'
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10) # 기다리고싶은 명령(get) 이전에 명시해주는듯?
browser.maximize_window() # 화면크기 최대화
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
imgs = browser.find_elements_by_css_selector('img._image._listImage')

for i, img in enumerate(imgs, 1):   # enumerate(대상, 시작값)
    # 각 이미지 태그의 주소
    img_src = img.get_attribute('src')
    print(i, img_src)
    # img를 index값의 파일명으로 png파일로 저장
    urllib.request.urlretrieve(img_src, f'실전편/03.네이버이미지_크롤링/{keyword}/{i}.png')