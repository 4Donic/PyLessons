from bs4 import BeautifulSoup
import requests
import re

from currency import currency


class UkrSibBank:
    __URL = 'https://ukrsibbank.com'

    def __get_html(self):
        resp = requests.get(self.__URL)
        return resp.text

    def get_currency_reta(self):
        curr_rate = {
            'rate': []
        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')
        # NALUSD
        contens = soup.find_all('div', id=re.compile('^NAL*'))

        for line in contens:
            currency_name = None
            for key, value in currency.items():
                if key.lower() in line['id'].lower():
                    currency_name = value

            if currency_name is None:
                continue

            curr_rate['rate'].append(
                {
                    'currency': currency_name,
                    'purchase_rate': line.find('div', class_='rate__buy').find('p').text.strip('\n').strip(),
                    'sale_rate': line.find('div', class_='rate__sale').find('p').text.strip('\n').strip(),
                }
            )
        return curr_rate


if __name__ == '__main__':
    us = UkrSibBank()
    print(us.get_currency_reta())
