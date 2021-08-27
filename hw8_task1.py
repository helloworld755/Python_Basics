import re

def email_parse(mail):
    try:
        re_email = re.split(r'@', mail)
        re_user = re.compile(r'^[A-Za-z0-9]+\B[A-Za-z0-9._]\B[A-Za-z0-9]+$')
        re_domain = re.compile(r'[a-zA-Z0-9-]+(?:\.[A-Za-z]{2,4})$')
        if re_user.match(re_email[0]) is not None and re_domain.match(re_email[1]) is not None:
            re_dict = {'username': re_email[0], 'domain': re_email[1]}
            print(re_dict)
        else:
            raise ValueError
    except ValueError:
        print(f'ValueError. Wrong email. Check again.')

email_parse('someone@geekbrains.ru')
