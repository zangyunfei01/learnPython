import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://list.tmall.com/search_product.htm?q=u%C5%CC&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=U_1&from=mallfp..pc_1_suggest")
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
for item in soup.select('.product-iWrap'):
    print(item.select('em')[0].text, item.select('.productShop-name')[0].text,
          item.select('.productStatus')[0].text.strip(), "\n")
