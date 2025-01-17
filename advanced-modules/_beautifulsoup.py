from bs4 import BeautifulSoup

html_doc = '''
<!doctype html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Web Scrapping</title>
</head>
<body>
<h1 id="header">Python Kursu</h1>
<div class="grup1">
    <h2>Programlama</h2>
    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
</div>

<div class="grup2">
    <h2>Modüller</h2>
    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
</div>

<div class="grup3">
    <h2>Django</h2>
    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
</div>

<img src="fred.png" alt="Fred Çakmaktaş">

<a class="sister" href="http://example.com/link1">Link 1</a>
<a class="sister" href="http://example.com/link2">Link 2</a>
<a class="sister" href="http://example.com/link3">Link 3</a>

</body>
</html>
'''

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()

result = soup.title
result = soup.head
result = soup.body

result = soup.title.string

result = soup.h1
result = soup.h2.name
result = soup.h2.string

result = soup.findAll('h2')[0]

result = soup.div
result = soup.findAll('div')[1]
result = soup.findAll('div')[1].ul
result = soup.findAll('div')[1].ul.li
result = soup.findAll('div')[1].ul.findAll('li')

result = soup.div.findChildren()

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.findAll('a')

for link in result:
    print(link.get('href'))
