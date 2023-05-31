import requests
from bs4 import BeautifulSoup

root = 'https://books.toscrape.com/'
links = []
for page in range(1, 2):
    result = requests.get(f'{root}catalogue/category/books_1/page-{page}.html')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    main_div = soup.find('section')
    hrefs = main_div.find_all('a', href=True)
    for h in hrefs:
        links.append((h['href'][6:-11]))
    linksnorep = list(dict.fromkeys(links))

    for link in linksnorep:
        try:
            result = requests.get(f'{root}catalogue/{link}/index.html')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            main_article = soup.find('article', class_="product_page")
            title = main_article.find('h1').get_text()
            available = main_article.find_all('tr')[5].findNext().findNext().get_text()
            description = main_article.find('div', id='product_description').findNextSibling().get_text(strip=True)

            with open(f'lesson_3_movies/{title.replace(":", "")}.txt', 'w', encoding='utf-8') as file:
                file.write(available + '\n\n' + description)

        except AttributeError:
            print('SKIP')
