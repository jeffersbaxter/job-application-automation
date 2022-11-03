import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2&keywords=python%20developer&sortBy=R")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(5)

user_field = driver.find_element(By.ID, "username")
user_field.send_keys(EMAIL)
pw_field = driver.find_element(By.ID, "password")
pw_field.send_keys(PASSWORD)
try:
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
except NoSuchElementException:
    print("Cant find sign in button")
    driver.quit()
else:
    sign_in_button.click()

    time.sleep(5)

    job_card_list = driver.find_elements(By.CSS_SELECTOR, "div.job-card-list")

    for job_card in job_card_list[:20]:
        try:
            job_card.click()
        except ElementClickInterceptedException:
            continue
        else:
            try:
                save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
            except NoSuchElementException:
                continue
            else:
                save_text = save_button.find_element(By.TAG_NAME, "span").text
                if save_text == "Save":
                    save_button.click()
        # try:
        #     easy_apply_button = driver.find_element(By.XPATH, '//*[@id="ember240"]/span')
        # except NoSuchElementException:
        #     continue
        # else:
        #     easy_apply_button.click()
        #     time.sleep(3)
        #     follow_company = driver.find_element(By.XPATH, '//*[@id="follow-company-checkbox"]')
        #     follow_company.click()
        #     try:
        #         submit = driver.find_element(By.XPATH, '//*[@id="ember403"]')
        #     except NoSuchElementException:
        #         continue
        #     else:
        #         submit.click()

    driver.quit()
