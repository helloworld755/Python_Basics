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
        # date from header
        print(f'Date from Header: {response.headers["Date"]}')
        # date from Body
        val_start = content.find('ValCurs Date="') + 14
        val_end = val_start + 10
        value = content[val_start:val_end]
        print(f'Date from Body: {str(value)}')
    else:
        print(f'{code.upper()}: None')
