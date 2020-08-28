import requests
from bs4 import BeautifulSoup

res = requests.get('http://book.naver.com')
print(res.text)

soup = BeautifulSoup(res.text)  # Soup 객체 반환

# Tag 객체 사용
a_tag = soup.a
print(type(a_tag))


# NavigableString 객체 사용
print(a_tag.prettify())
