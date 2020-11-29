from bs4 import BeautifulSoup
import requests

base_url = 'http://dh.aks.ac.kr/Encyves/wiki/index.php/조선_세종'
con = requests.get(base_url)
soup = BeautifulSoup(con.content, 'lxml')

infoTable = soup.find("table",{"class":"wikitable sortable"})  #테이블 태그중 클래스가 wikitable sortable인 것만 찾기
infoPrint =[]
for a in infoTable.find_all("tr"):    #wikitable sortable이라는 이름의 테이블에서 모든 tr태그(행)를 반복해서 불러오기
    infolist = []
    for b in a.find_all("td"):        #모든 tr태그(행)마다 모든 td태그(열)을 반복해서 불러오기
        info = b.get_text()           #td 값의 텍스트 추출
        infolist.append(info)         #추출한 텍스트를 리스트에 저장
    infoPrint.append(infolist)
print(infoPrint)
