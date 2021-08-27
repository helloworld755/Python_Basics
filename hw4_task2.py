import requests as rq
from decimal import Decimal


def currency_rates(code):
    response = rq.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = rq.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    start = content.find(code.upper())
    if start != -1:
        val_start = content.find("<Value>", start, len(content)) + 7
        val_end = content.find("</Value>", start, len(content))
        value = content[val_start:val_end]
        print(f'{code.upper()}: {str(Decimal(value.replace(",", ".")))}')
    else:
        print(f'{code.upper()}: None')


if __name__ == '__main__':
    currency_rates("UsD")
    currency_rates("euR")
    currency_rates("ABc")
