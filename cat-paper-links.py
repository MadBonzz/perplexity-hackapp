import requests
from bs4 import BeautifulSoup

url = "https://online.2iim.com/CAT-question-paper/"

# Fetch the page content
response = requests.get(url)
response.raise_for_status()  # Raises an error for bad responses

soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'col_one_sixth' (including those with additional classes like 'col_last')
divs = soup.find_all('div', class_='col_one_sixth')

links = []
for div in divs:
    a_tag = div.find('a', href=True)
    if a_tag:
        links.append(a_tag['href'])

print(len(links))

with open('mba_links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
