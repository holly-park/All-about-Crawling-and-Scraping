import requests        #http request를 요청한다
from bs4 import BeautifulSoup     

r = requests.get('<웹 사이트 주소 URL>')     #해당 URL 주소를 가져온다

print(r)  #응답코드를 가져온다(확인이 매우 중요하다)

html = req.text                             #html 소스를 가져온다

#(html코드, 사용할 parser) 첫번째 인자와 두번째 인자값을 준다
soup = BeautifulSoup(html, 'html parser')  


#아래에 가져오고 싶은 요소를 붙여넣는다
