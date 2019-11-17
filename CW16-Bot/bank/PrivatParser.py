import requests
from currency import currency

class PrivateParser:
    __URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    def __get_json(self):
        resp = requests.get(self.__URL)
        return resp.json()

    def get_currency_reta(self):
        curr_rate = {
            'rate': []
        }

        result = self.__get_json()
        for line in self.__get_json():
            if line['ccy'].strip().lower() in currency.keys():
                curr_rate['rate'].append(
                    {
                        'currency': currency.get(line['ccy'].lower()),
                        'purchase_rate': str(round(float(line['buy']), 2)),
                        'sale_rate': str(round(float(line['sale']), 2)),
                    }
                )
        return curr_rate


if __name__ == '__main__':
    pb = PrivateParser()
    print(pb.get_currency_reta())