import bs4
import requests
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
two_star_rated = []
for i in range(1,51):
    res = requests.get(base_url.format(i))    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    products = soup.select('.product_pod')
    for product in products:
        if product.select('.star-rating.Two'):
            two_star_rated.append(
                str(product.select('a')[1]['title'])
            )


for i in two_star_rated:
    print(i)


