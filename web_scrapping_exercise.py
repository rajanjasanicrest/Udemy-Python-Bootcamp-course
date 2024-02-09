import bs4
import requests

# task 1 : Use requests and bs4 to connect to https://quotes.toscrape.com/
res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')

# Task2 : Get the name of all the authors on the first page
res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
ele = soup.select('.author')
authors = [x.text for x in ele]
print(set(authors))


# Task3 : Get all the quotes on the first page
res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
ele = soup.select('.quote')
quotes = [x.select('.text')[0].text for x in ele]
for quote in quotes:
  print(quote)


# Task 4: Return top 10 tags on quotes home page
res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
tags_list = set()
elements = soup.select('.tags')
for element in elements:
  for sub_element in element.select('.tag'):
    tags_list.add(sub_element.text)
tags_list = list(tags_list)
for tag in tags_list[:10]:
  print(tag)


#task 5:  https://quotes.toscrape.com/page/1/ get list of all the unique authors across all the pages:
base_url = 'https://quotes.toscrape.com/page/{}/'
i = 1
while True:
  res = requests.get(base_url.format(i))
  soup = bs4.BeautifulSoup(res.text,'lxml')
  ele = soup.select('.author')
  if len(ele) == 0:
    break
  authors += [x.text for x in ele]
  i+=1 
authors = list(set(authors))
for author in authors:
  print(author)