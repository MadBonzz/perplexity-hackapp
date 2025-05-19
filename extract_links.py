from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from tqdm import tqdm

driver = webdriver.Chrome()

with open('gre_links.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

result = {}
elements = soup.find_all(['h2', 'ul'])

current_title = None

for el in elements:
    if el.name == 'h2':
        a_tag = el.find('a')
        if a_tag:
            current_title = a_tag.get_text(strip=True)
    elif el.name == 'ul' and current_title:
        links = []
        for li in el.find_all('li'):
            a = li.find('a', href=True)
            if a:
                links.append(a['href'])
        result[current_title] = links
        current_title = None  

questions_dict = []

for key in tqdm(result.keys()):
    topic_links = result[key]
    for link in topic_links:
        url = 'https://www.manhattanreview.com/' + link
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        question = wait.until(
            EC.presence_of_element_located((By.ID, "wf_qb_question"))
        ).text

        option_elements = driver.find_elements(By.CSS_SELECTOR, "#wf_qb_answer_input .wf_qb_answer_row")
        options = [opt.text for opt in option_elements]
        ques = {'question' : question, 'options' : options, 'type' : key}
        questions_dict.append(ques)

df = pd.DataFrame(questions_dict)
df.to_csv('gre_questions.csv')
