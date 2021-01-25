import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random

link = "https://browser-info.ru/"

header = {
    "user-agent": user
}

response = requests.get(link,
                        headers=header).text


soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='tool_padding')

# Check JS
check_js = block.find('div',
                      id='javascript_check').find_all('span')[1].text

print('JS :', check_js)


# Check User-Agent
check_user_agent = block.find('div',
                              id='user_agent').text

print(check_user_agent)