from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='drivers/chromedriver')

driver.get('https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=15524934075')

driver.close()