from selenium import webdriver
from bs4 import beautifulSoup

driver = webdriver.Chrome('<크롬드라이버 경로>/chromedriver')

driver.implicitly_wait(3)  ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.get('https://nid.naver.com/nidlogin.login')


## 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')

## 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())
