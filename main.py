from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
button = browser.find_element(By.ID, 'book')
button.click()


x = int(browser.find_element(By.ID, "input_value").text)
y = calc(x)
print(y)


input1 = browser.find_element(By.TAG_NAME, 'input')
input1.send_keys(y)


button1 = browser.find_element(By.ID, 'solve')
button1.click()




