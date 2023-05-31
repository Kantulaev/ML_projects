import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
content = result.text
soup = BeautifulSoup(content, 'lxml')

left_section = soup.find('div', class_='sphinxsidebar').get_text(strip=True, separator=' ')
title = soup.find('h1').get_text()
# paragrafs = left_section.find('p').get_text(strip=True,separator=' ')
# for p in paragrafs:
#     print(p.get_text(strip=True,separator=' '))

# print(title.prettify())
print(left_section)
print(title)

with open(f'{title}.txt', 'w') as file:
    file.write(left_section)
