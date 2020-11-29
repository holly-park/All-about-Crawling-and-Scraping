import requests        #http request를 요청한다
from bs4 import BeautifulSoup     

r = requests.get('<웹 사이트 주소 URL>')     #해당 URL 주소를 가져온다

print(r)  #응답코드를 가져온다(확인이 매우 중요하다)

html = req.text                             #html 소스를 가져온다

#(html코드, 사용할 parser) 첫번째 인자와 두번째 인자값을 준다
soup = BeautifulSoup(html, 'html parser')  


#아래에 가져오고 싶은 요소를 붙여넣는다

#1.css selector   --> body > h3:nth-child(4) > a    이것은 (4)의 요소를 정확하게 특정하고 있기 때문에 h3 > a  로 바꾸는게 나을 수 있다
                      #my_titles = soup.select('h3 > a')
## my_titles는 list 객체
for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))
    
 
#result.json 파일을 만들어서 저장하기
data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
    
    
