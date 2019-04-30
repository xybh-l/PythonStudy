from bs4 import BeautifulSoup
html_sample = ' \
<html> \
<body> \
<h1 id="title">Hello World</h1> \
<a href="#" class="link">This is link1</a> \
<a href="# link2" class="link">This is link2</a> \
</body> \
</html>'
a = '<a href="#" qoo=123 abc=456> i am a link </a>'
soup = BeautifulSoup(html_sample,'html.parser')
soup2 = BeautifulSoup(a,'html.parser')

# header = soup.select('h1')
# print(header)
# alink = soup.select('#title')
# print(alink)
# alinks = soup.select('a')
# for link in alinks:
#     print(link['href'])
# # alink = soup.select('a')
# # print(alink)
# print(soup.text)
print(soup2.select('a'))