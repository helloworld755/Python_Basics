def add_sale(argv):
    program, text = argv
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(text+'\n')
    return 0


if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))
