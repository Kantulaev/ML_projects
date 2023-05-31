import requests
from bs4 import BeautifulSoup

root = 'http://geekwriter.ru/'
result = requests.get(f'{root}blog.html#blog')
content = result.text
soup = BeautifulSoup(content, 'lxml')

links = []
main_div = soup.find('div', class_='toctree-wrapper compound')
links_main_div = main_div.find_all('a', href=True)
for link in links_main_div:
    links.append(link['href'])

for link in links:
    result = requests.get(f'{root}{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    main_div = soup.find('div', class_='body')
    title = main_div.find('h1').get_text()

    with open(f'{title}.txt', 'w') as file:
        file.write(main_div.get_text())
