from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://www.youtube.com/")

# time.sleep(5) 실행도중 페이지 로딩시간 충분히 주기위해 잠시 멈추기

driver.implicitly_wait(3)   # 드라이브가 로딩되는 중 3초 기다렸다가 한다.


search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('김계란')
search.send_keys(Keys.ENTER)
driver.implicitly_wait(3)

# 8개 더보기 버튼 눌러서 동영상 리스트 펼치기
driver.find_element_by_css_selector('#more > yt-formatted-string > span:nth-child(3)').click()
driver.implicitly_wait(3)

# 타이틀
# title_list = []
# titles = driver.find_elements_by_css_selector('#video-title > yt-formatted-string')
# for t in titles:
#     print(t.text)
#     title_list.append(t.text)

# 동영상 링크
yt_links = []
thumbs = driver.find_elements_by_css_selector('#thumbnail')
for th in thumbs:
    print(th.get_attribute('href'))
    yt_links.append(th.get_attribute('href'))