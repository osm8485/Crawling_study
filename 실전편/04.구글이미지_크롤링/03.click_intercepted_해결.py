from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request  # 이미지 저장 모듈



if not os.path.exists(f'실전편/04.구글이미지_크롤링/고양이'):   # 해당 폴더의 존재여부를 boolean값으로 출력해줌
    # not True = False : 해당폴더가 기존에 존재하지 않으면 새 폴더를 만든다!
    os.mkdir(f'실전편/04.구글이미지_크롤링/고양이')  

url = f'https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&rlz=1C5CHFA_enKR989KR989&hl=ko&sxsrf=APq-WButoPiENxH9X9ZeW8BqecgmAOfkRQ:1643789118040&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi7id3Tx-D1AhV9slYBHZMTAusQ_AUoAXoECAIQAw&biw=1512&bih=833&dpr=2'
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10) # 기다리고싶은 명령(get) 이전에 명시해주는듯?
# browser.maximize_window() # 화면크기 최대화
browser.get(url)  

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

# 썸네일 이미지 태그 추출
imgs = browser.find_elements_by_css_selector('.rg_i.Q4LuWd')

for i, img in enumerate(imgs, 1):   # enumerate(대상, 시작값)
    # 이미지를 클릭해서 큰 사이즈를 찾아요
    # 클릭하다보면 element click intercepted 에러가 나요
    # javascript로 클릭을 직접 하도록 만들어주면 됩니다.
    browser.execute_script("arguments[0].click();", img)
    time.sleep(1)
    img_src = img.get_attribute('src')
    # 큰 이미지 주소 추출
    if i == 1 :
        target = browser.find_elements_by_css_selector('img.n3VNCb')[0]
    else:
        target = browser.find_elements_by_css_selector('img.n3VNCb')[1]
    
    img_src = target.get_attribute('src')
    
    # 이미지 다운로드
    # 크롤링 하다보면 HTTP Error 403: Forbidden 에러가 날 때가 있다. >> 봇으로 인식하여 자동차단
    # bs4에서 request.get요청에 headers 추가한 것 처럼 여기서도 추가해준다!
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(img_src, f'실전편/04.구글이미지_크롤링/고양이/{i}.jpg')
    urllib.request.urlretrieve(img_src, f'실전편/04.구글이미지_크롤링/고양이/{i}.jpg')
    
   
