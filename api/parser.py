import requests
from bs4 import BeautifulSoup
import fake_useragent


class BookScrapper:
    def __init__(self):
        self.url = "https://www.yakaboo.ua/ecomdev_catalog/ajax/now_buying/"
        self.user = fake_useragent.UserAgent().random

        self.header = {
            'user-agent': self.user,
            'accept': "text/javascript, text/html, application/xml, text/xml, */*",
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'refer': 'https://www.yakaboo.ua/jelektronnye-knigi/hudozhestvennaja-literatura.html',
            'cookie': '__cfduid=d78cdd1b8a6d118e02f466482d871a8e91611734956; frontend=3cefdd7e120042008f157d696892e4f6; _gid=GA1.2.2000544936.1611734957; serverVisitorGroup=2; collect-emails-timer=1611734957103; _gcl_au=1.1.1367310612.1611734957; gtm_isNewVisitor=1; gtm_visitorGroup=5; is_logged_in=0; visit_first_time=1611734957; d90=1; d1=1; sc=90CC05BF-D2B5-ABA4-CEB7-15BB46AE8583; _fbp=fb.1.1611734957718.2107785583; _hjTLDTest=1; _hjid=c112697e-2353-4f8c-8892-4e85591b6ccb; _hjFirstSeen=1; _pk_ref.1.0426=%5B%22%22%2C%22%22%2C1611734958%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.0426=*; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0; gravitecOptInBlocked=true; LastVisitedUrl=%2Fjelektronnye-knigi%2Fhudozhestvennaja-literatura.html; AffinityL1Cat=%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5+%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8; _pk_id.1.0426=5b6e3473855e6eb5.1611734958.1.1611735122.1611734958.; collect-emails-timer-popup=1611735250293; _gat=1; _gat_UA-6675819-8=1; _gat_UA-6675819-1=1; _ga_NLRLPV7JQ4=GS1.1.1611734957.1.1.1611735570.0; _ga=GA1.2.1869437185.1611734957; gtm_is25th=4'
        }

        self.data = {
            'categoryId': 8855
        }

    def parse(self):
        response = requests.post(self.url,
                                 self.data,
                                 headers=self.header)

        return (
            {
                "url": item.find('a', {
                    "class": "product-name"
                })['href'],
                "title": item.find('a', {
                    "class": "product-name"
                }).text,
                'author': item.find('div', {
                    'class': "product-author"
                }).text,
                'price': ' '.join(item.find('div', {
                    'class': "price"
                }).text.split('\xa0'))
            } for item in BeautifulSoup(response.text,
                                        'lxml').find_all('div', {'class': 'caption'})
        )


def facebook_ads():
    url = 'https://www.facebook.com/ads/library/async/search_ads/?session_id=2fb58586-b5b3-4530-9c91-9cfca8a45982&count=30&active_status=all&ad_type=all&countries[0]=ALL&view_all_page_id=27682782579'
    data = {
        '__user': '0',
        '__a': '1',
        '__dyn': '7xeUmBwjbgydwCwRyWwHBWo5O12wAxu13wqojyUW3qi2K7EiwvoWdwJx63C3qcw9m3y4o3Bw5VCwjE3awbG782Cwoovy8465o-cw5MKi8wl8G0DE7e2l0FG7o4y0Mo5Wm588Etw8WfxW1kwPxe0REsVobobEaUtx-1gwnE2Wyo9UC',
        '__csr': '',
        '__req': '1',
        '__beoa': '0',
        '__pc': 'PHASED:DEFAULT',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1003227765',
        '__s': '::zridk7',
        '__hsi': '6922448248926373632-0',
        '__comet_req': '0',
        'lsd': 'AVopUYoTdvc',
        'jazoest': '21060',
        '__spin_r': '1003227765',
        '__spin_b': 'trunk',
        '__spin_t': '1611758081'
    }

    header = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '423',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=27682782579',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'User-Agent': fake_useragent.UserAgent().random,
            'Accept-Encoding': 'gzip, deflate',
        }
    res = requests.post(url, data=data, headers=header)
    x = res.text
    print(x)


if __name__ == "__main__":
    facebook_ads()
