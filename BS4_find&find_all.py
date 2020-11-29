from bs4 import BeautifulSoup     

r = requests.get('<웹 사이트 주소 URL>')     #해당 URL 주소를 가져온다

print(r)  #응답코드를 가져온다(확인이 매우 중요하다)

html = req.text                             #html 소스를 가져온다

#(html코드, 사용할 parser) 첫번째 인자와 두번째 인자값을 준다
soup = BeautifulSoup(html, 'html parser')  


#find: 첫번째 TAG를 리턴
#findAll: 조건에 해당하는 모든 TAG를 리스트 형태로 리턴

html_str = '''
<html>
    <body>
        <img src="path1" alt="테스트 이미지_1" />
        <img src="path2" alt="테스트 이미지_2" />
        <img src="path3" alt="테스트 이미지_3" />
    </body>
</html>
'''

imgtag = soup.find('img')
print(imgtag['alt'])    #테스트 이미지_1



imgtag = soup.findAll('img')
 
#print(imgtag[0].get_text())  첫번째 요소만 프린트 하고 싶을 경우
for tag in imgtag:
    print(tag['alt'])   #테스트 이미지_1
                        #테스트 이미지_2
                        #테스트 이미지_3
            


