from selenium import webdriver

driver = webdriver.Chrome('<크롬드라이버 경로>/chromedriver')

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

driver.get('https://google.com')
