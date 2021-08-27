import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def parsed_raw(t):
    list_t = t.splitlines()
    for el in list_t:
        re_el = re.search(r'(\d{1,4}\.){3}\d{1,4}', el)
        if re_el is not None:
            re_el_2 = re.search(r'(\d{,2}/)([A-Za-z]{3})/(\d{4}:\d{2}:\d{2}:\d{2})\s([0-9+]{5})', el)
            if re_el_2 is not None:
                re_el_3 = re.search(r'GET', el)
                if re_el_3 is not None:
                    re_el_4 = re.search(r'/downloads/product_[0-9]{1}', el)
                    if re_el_4 is not None:
                        re_el_5 = re.search(r'HTTP/1.1"\s([0-9]{,3}\s([0-9]{,8}))', el)
                        if re_el_5 is not None:
                            re_el_6 = re_el_5.group(0).split(sep=' ')
                            print((re_el.group(0), re_el_2.group(0), re_el_3.group(0), re_el_4.group(0), re_el_6[1], re_el_6[2]))

parsed_raw(text)
