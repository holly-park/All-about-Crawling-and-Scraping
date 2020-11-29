# All-about-Crawling-and-Scraping


---

데이터 분석을 하기 위에서 REST API 또는 웹 상의 정보를 가져오는 것은 거의 필수라고 할 수 있다. 이 때 Python으로 Beautifulsoup이나 Selenium 같은 라이브러리를 쓰고는 한다. 이때 시도해 볼 수 있는 Tag나 element를 가져오는 것을 표현하는 방식을 각각 정리함과 동시에 Beautifulsoup을 사용할 때와 Selenium을 사용할 때의 장단점을 비교해보려고 한다.


---

[크롤링과 스크레이핑의 차이점은 뭘까?]
크롤링(crawling)은 정기적으로 웹페이지를 순회하기 때문에 최신의 정보를 다운로드하고 정확히 유지할 수 있다. 한편, 스크레이핑(scraping)은 웹페이지의 구조로부터 특정 데이터를 추출하는 것을 말한다.

urllib: HTTP 나 FTP를 활용하여 데이터를 다운로드 한다. 그 중에서도 urllib.request는 웹상에있는 데이터에 접근이 가능하다. Authorization, Redirect, Cookie처럼 다양한 요청과 처리를 지원하기도 한다. Get방식은 Http Header에 포함하여 데이터를 전송하고, Post방식은 HTTP Body포함하여 데이터를 전송한다

Beautifulsoup은 데이터를 웹상으로부터 스크레이핑하기 위한 파이썬 라이브러리이다.

a.get('href')   -----------> 태그 a에서 href 속성의 값(하이퍼링크 url) 추출 

soup.title.name    --------> title태그의 이름 title 추출하기  

soup.title.string  --------> title 태그의 문자값 추출하기  

soup.find(id="link")  -----> id가 link인 태그와 값을 추출하기  

soup.TagName.parent   -----> 특정 태그의 상위 태그 값 추출하기   

soup.find_all("a", limit=2)    ---->  2개만 가져오기

soup.title.find_all(string=True)   ---->  title에서 String만 가져오기

soup.find_all("p", "title")    ----> P태그이면서 class(속성 값)이 title인 것

soup.find_all(["a", "b"])    ----->  or 조건(a태그이거나 b태그인 것)

soup.body.b     ------>  body 태그 아래의 첫번째 b 태그

**bs의 select 사용법**
soup.select('태그')
soup.select('.클래스명') 혹은 ('태그.클래스명')
soup.select('#아이디명') 혹은 ('태그#아이디명')
soup.select('태그 > 자식태그')
soup.select('태그 자손태그')



