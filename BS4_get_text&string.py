from bs4 import BeautifulSoup     

r = requests.get('<웹 사이트 주소 URL>')     #해당 URL 주소를 가져온다

print(r)  #응답코드를 가져온다(확인이 매우 중요하다)

html = req.text                             #html 소스를 가져온다

#(html코드, 사용할 parser) 첫번째 인자와 두번째 인자값을 준다
soup = BeautifulSoup(html, 'html parser')


html = \
"""
<div class="item_price">
    <div class="o-price">
        <span><27,000원</span>
    </div>
    <div class="s-price">
        <strong><span>12,900원</span></strong>
    </div>
</div>
"""

#get_text() : html내의 모든 text 추출
#string: 정확하게 문자열 추출

soup.select_one('.item_price').get_text()   # '\n\n<27,000원\n\n\n12,900원\n\n'
soup.select_one('.item_price > .s-price span').get_text()          #'12,900원'

soup.select_one('.s-price > strong > span').string   #'12,900원'
#태그가 자식내에 둘이상이면 None값을 반환한다
soup.select_one('.s-price').string                   # None          
soup.select_one('.s-price > strong').string          #'12,900원'

