from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json


d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'performance': "ALL"}


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(executable_path='drivers/chromedriver',
                          desired_capabilities=d,
                          options=chrome_options)

driver.get('https://www.yakaboo.ua/jelektronnye-knigi/hudozhestvennaja-literatura.html')

for i in range(1):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'product-list_show-more')
            )
        )
        element.click()
    except:
        print('error')
        driver.close()
    finally:
        for entry in driver.get_log('performance'):
            x = json.loads(entry)
            print(x)

driver.close()
