def book_info(soup):
      url = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query=' + txt
    req = requests.get(url)
	soup = BS(req.text, 'html.parser')
    info = {}
    con = soup.find('div', {'class':'book_info'})
    inner = soup.select('.book_info_inner > div')[1]
    info['title'] = con.select_one('h2 > a').text
    info['img'] = con.select_one('.thumb_type img')['src']
    info['auth'] = inner.select('a')[0].text
    info['pub'] = inner.select('a')[1].text
    bID = soup.select_one('.book_info_inner')
    
return info
