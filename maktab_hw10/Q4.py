import requests
from bs4 import BeautifulSoup
# problem
# url='https://virgool.io/@asamasach/%DA%86%D8%B1%D8%A7-%D8%A7%D8%B2-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D9%85%D8%AA%D9%86%D9%81%D8%B1%D9%85-yj3zebvieybc'
# response=requests.get(url)
# print(response)
# print(response.text)
############
url = 'https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D8%AF%D8%B1%DB%8C%DA%A9_%D9%87%D8%B1%D8%B2%D8%A8%D8%B1%DA%AF'
res = requests.get(url)
# print(res.text)
bs = BeautifulSoup(res.text, 'html.parser')
result = bs.find_all('p')
print(result)










