from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.manhattanreview.com/gre-practice-questions/35/")
    wait = WebDriverWait(driver, 10)

    question = wait.until(
        EC.presence_of_element_located((By.ID, "wf_qb_question"))
    ).text

    option_elements = driver.find_elements(By.CSS_SELECTOR, "#wf_qb_answer_input .wf_qb_answer_row")
    options = [opt.text for opt in option_elements]

    if option_elements:
        option_elements[0].click()
        option_elements[1].click()
    else:
        raise Exception("No options found.")

    submit_button = driver.find_element(By.CLASS_NAME, "wf_qb_question_submit")
    submit_button.click()

    time.sleep(2)
    EC.element_to_be_clickable((By.CLASS_NAME, "swal-button swal-button--custom1"))
    
    time.sleep(1)
    answer = ""
    explanation = ""
    try:
        answer = driver.find_element(By.CSS_SELECTOR, ".correct-answer, .wf_qb_answer_correct").text
    except:
        pass
    try:
        explanation = driver.find_element(By.CSS_SELECTOR, ".explanation-text, .wf_qb_explanation").text
    except:
        pass

    print("Question:", question)
    print("Options:", options)
    print("Answer:", answer)
    print("Explanation:", explanation)

finally:
    driver.quit()
