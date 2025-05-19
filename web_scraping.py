import requests
from bs4 import BeautifulSoup

urls =  {"cat-2018-lrdi-1" : "https://bodheeprep.com/cat-2018-lrdi-question-paper-with-solution-slot-1",
         "cat-2018-lrdi-2" : "https://bodheeprep.com/cat-2018-lrdi-question-paper-with-solution-slot-2",
         "cat-2018-quant-1" : "https://bodheeprep.com/cat-2018-quant-question-paper-slot-1",
         "cat-2018-quant-2" : "https://bodheeprep.com/cat-2018-quant-question-paper-slot-2",
         "cat-2018-varc-1" : "https://bodheeprep.com/cat-2018-varc-question-paper-with-solution-slot-1",
         "cat-2018-varc-2" : "https://bodheeprep.com/cat-2018-varc-question-paper-with-solution-slot-2",
         "cat-2019-varc-1" : "https://bodheeprep.com/cat-2019-varc-question-paper-with-solutions-slot-1",
         "cat-2019-varc-2" : "https://bodheeprep.com/cat-2019-varc-question-paper-with-solutions-slot-2",
         "cat-2019-quant-1" : "https://bodheeprep.com/cat-2019-quant-question-paper-slot-1",
         "cat-2019-quant-2" : "https://bodheeprep.com/cat-2019-quant-question-paper-slot-2",
         "cat-2020-quant-1" : "https://bodheeprep.com/cat-2020-quant-question-paper-slot-1",
         "cat-2020-quant-2" : "https://bodheeprep.com/cat-2020-quant-question-paper-slot-2",
         "cat-2020-quant-3" : "https://bodheeprep.com/cat-2020-quant-question-paper-slot-3",
         "cat-2020-varc-1" : "https://bodheeprep.com/cat-2020-varc-questions-solutions-slot-1",
         "cat-2020-varc-2" : "https://bodheeprep.com/cat-2020-varc-questions-solutions-slot-2",
         "cat-2020-varc-3" : "https://bodheeprep.com/cat-2020-varc-questions-solutions-slot-3",
         "cat-2021-varc-1" : "https://bodheeprep.com/cat-2021-varc-questions-solutions-slot-1",
         "cat-2021-varc-2" : "https://bodheeprep.com/cat-2021-varc-questions-solutions-slot-2",
         "cat-2021-varc-3" : "https://bodheeprep.com/cat-2021-varc-questions-solutions-slot-3",
         }

for url in urls.keys():
    response = requests.get(urls[url])
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    target_div = soup.find(
        "div",
        class_="elementor-element elementor-element-7a0a590 elementor-widget elementor-widget-theme-post-content"
    )

    if target_div:
        with open(f"cat-questions/{url}.html", "w", encoding="utf-8") as f_html:
            f_html.write(target_div.prettify())
    else:
        print("Target div not found.")
