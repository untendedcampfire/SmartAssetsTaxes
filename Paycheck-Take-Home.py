# Selenium used to find the take home pay and respective taxes in Arizona for a range of different income
# Assumptions:
# Location = Chandler, AZ
# State percentage = 2.7%
# Pay Frequency = Bi-Weekly
# Allowances = 1 1 1 (Fed, State, Local)
# No additional withholding
# No pre-tax deductions

import numpy as np
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep, time

TAXES_URL = "https://smartasset.com/taxes/arizona-paycheck-calculator"

# salary_range = np.arange(40000, 121000, 1000).tolist()
salary_range_lg = np.arange(20000, 200000, 100).tolist()
# salary_range_smol = np.arange(40000, 50000, 1000).tolist()

paycheck_list = []
percentage_list = []


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(TAXES_URL)
sleep(1)
text_bar = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/div/span/input")
for salary in salary_range_lg:
    text_bar.clear()
    sleep(1)
    text_bar.send_keys(str(salary))
    text_bar.send_keys(Keys.ENTER)
    sleep(1)
    percentage = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[4]/div[1]/table/tfoot/tr/td[3]/span")
    dollar = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[4]/div[1]/table/tfoot/tr/td[4]/span")
    percentage_list.append(percentage.text)
    paycheck_list.append(dollar.text)

with open("take_home_dump", "wb") as fp:
    pickle.dump(paycheck_list, fp)
with open("percentage_dump", "wb") as fp:
    pickle.dump(percentage_list, fp)

while True:
    pass