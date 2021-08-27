import yaml
import os

with open('config.yaml') as f:
    conf = yaml.safe_load(f)

'''
{'my_project':
     {'authapp':
          ['__init.py__',
           'models.py',
           'views.py',
           {'templates':
                {'authapp':
                     ['base.html',
                      'index.html']}}],
      'mainapp':
          ['__init.py__',
           'models.py',
           'views.py',
           {'templates':
                {'mainapp':
                     ['base.html',
                      'index.html']}}],
      'settings':
          ['__init.py__',
           'dev.py',
           'prod.py']}}
'''


def rek(a, from_dir='./'):
    if type(a) == dict:
        for key, val in a.items():
            os.mkdir(os.path.join(from_dir, key))
            if type(val) == dict:
                rek(val, os.path.join(from_dir, key))
            elif type(val) == list:
                rek(val, os.path.join(from_dir, key))
    elif type(a) == list:
        for el in a:
            if type(el) == str:
                with open(os.path.join(from_dir, el), "w"):
                    pass
            elif type(el) == dict:
                for key, val in el.items():
                    os.mkdir(os.path.join(from_dir, key))
                    if type(val) == dict:
                        rek(val, os.path.join(from_dir, key))
                    elif type(val) == list:
                        rek(val, os.path.join(from_dir, key))


rek(conf)
