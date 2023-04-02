import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


first_paragraph = soup.find('p')
print(first_paragraph.text)


headings = soup.find_all('h2')
for heading in headings:
    print(heading.text)


toc = soup.find(id='toc')
links = toc.find_all('a')
for link in links:
    print(link.text)
