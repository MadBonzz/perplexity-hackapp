import requests
from bs4 import BeautifulSoup

links = []
link_path = 'mba_links.txt'
with open(link_path, 'r') as file:
    links = file.readlines()

clean_links = []
for link in links:
    if(('DILR'  in link) or ('XAT' in link)):
        link = link[:-2]
        clean_links.append(link)
print(clean_links)

for link in clean_links:
    response = requests.get(link)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    target_div = soup.find(
        "div",
        class_="col span_4_of_5"
    )

    if target_div:
        with open(f"mba-pyq/{link.split('/')[-1]}.html", "w", encoding="utf-8") as f_html:
            f_html.write(target_div.prettify())