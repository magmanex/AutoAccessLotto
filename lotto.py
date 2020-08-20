from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

while True:
    try:
        driver.get("https://www.lotto.ktbnetbank.com/KTBLotto/#/login")
        elem = driver.find_element_by_class_name("login-h1")
        print(elem)
        break
    except KeyboardInterrupt:
        print('interrupted!')
        break
    except :
        time.sleep(0.5)
        driver.delete_all_cookies()
        pass
