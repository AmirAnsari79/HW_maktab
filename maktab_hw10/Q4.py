import requests
from bs4 import BeautifulSoup

url = 'https://virgool.io/@asamasach/%DA%86%D8%B1%D8%A7-%D8%A7%D8%B2-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D9%85%D8%AA%D9%86%D9%81%D8%B1%D9%85-yj3zebvieybc'
res = requests.get(url)
bs = BeautifulSoup(res.text, 'html.parser')
# x = bs.find('p', {'class': 'md-block-unstyled md-block-rtl'})
x = bs.select_one('p.md-block-unstyled md-block-rtl')
print(x.text.strip())
