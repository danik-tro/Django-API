import requests
from bs4 import BeautifulSoup


class BookScrapper:
    def __init__(self):
        self.url = "https://www.yakaboo.ua/ecomdev_catalog/ajax/now_buying/"

    @staticmethod
    def parse_category():
        url = 'https://www.yakaboo.ua/turpentine/esi/getBlock/method/ajax/access/public/ttl/86400/hmac' \
              '/de5b40ce60ee3063daf4c4b18d2478865aed3c2c499ae4610a715cf21e41b421/data/8IdU5MU' \
              '.mHolXJUYyPlfRkZoWnk8B83T7dc2umcJIz3gAzFllZ62vNfZ2HiwkghDpldBakwGwH6hgouRWm9Sk61aH.c28wseiCpTBms' \
              '.ZSSIBmzOoaNO69JH-PsrfP8339AXSB5jFzR0yIgHgzkA' \
              '-SxcdTMIjnLHs7zppDHoArkv3IefW9iLN3kiSrHdmDclzd6n123bGtggXJZJxU5PQY3meKwDU' \
              '-ckTR57gY7CwGH08dibkvPC0BQN4bmiGOhiJqeWgbnKE7Q   bfEIeHnGSZqkxWJUoeGDLxnK.u2U-NNOrx.CXagcURg==/'

        div_books = BeautifulSoup(requests.get(url).text,
                                  'lxml').find_all('div',
                                                   'sub-categories')[0]

        return ({
            "url": item['href'],
            "name": item.text
        } for item in div_books.find_all('a'))

    @staticmethod
    def parse_content(url):
        response = requests.get(url)

        return (
            {
                "url": item.find('a', {
                    "class": "product-name"
                })['href'],
                "title": ' '.join(item.find('a', {
                    "class": "product-name"
                }).text.split()),
                'author': ' '.join(item.find('div', {
                    'class': "product-author"
                }).text.split()),
                'price': ' '.join(' '.join(item.find('div', {
                    'class': "price"
                }).text.split('\xa0')).split())
            } for item in BeautifulSoup(response.text,
                                        'lxml').find_all('div', {'class': 'caption'})
        )


def facebook_ads():
    data = {
        '__user': '0',
        '__a': '1',
        '__dyn': '7xeUmBwjbgydwn8KEaVuC1swgE98nwgU6C4UKewSAwHxW4E7SezobohwVwSz82lwUx60Vo1upE4W0OE2WxO0FE667Uy11xmfz81sbAy85iaw9W1PwBgaqxS18wc61uBxi2a7o2ezUuwl8cUjwdq7em2S2W2K7ovwk85W0KEC2u9w',
        '__csr': '',
        '__req': 'd',
        '__beoa': '0',
        '__pc': 'PHASED:DEFAULT',
        'dpr': '1.5',
        '__ccg': 'EXCELLENT',
        '__rev': '1003233634',
        '__s': 's2eit0:ovrjdb:c5m410',
        '__hsi': '6922735533724091960-0',
        '__comet_req': '0',
        'lsd': 'AVpMrGKqrSM',
        'jazoest': '2987',
        '__spin_r': '1003233634',
        '__spin_b': 'trunk',
        '__spin_t': '1611824970'
    }
    url = 'https://www.facebook.com/ads/library/async/search_ads/?session_id=fa050d21-f56b-4752-8d96-566d858fb6da' \
          '&count=1&active_status=all&ad_type=all&countries[0]=ALL&view_all_page_id=15524934075'

    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '470',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.facebook.com',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=15524934075&publisher_platforms[0]=facebook',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
    }
    res = requests.post(url, data=data, headers=header)
    res = requests.post(url, data=data, headers=header)
    x = res.text
    print(x)


if __name__ == "__main__":
    print(list(BookScrapper().parse_content('https://www.yakaboo.ua/knigi/samorazvitie-motivacija.html?p=1&is_ajax=1')))