from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.youtube.com/results?search_query=%EB%8F%88%EB%B2%84%EB%8A%94%EB%B2%95')
browser.implicitly_wait(10)

