import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')


image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
image_link.content

f = open('muimg.jpg','wb')
f.write(image_link.content)
f.close()