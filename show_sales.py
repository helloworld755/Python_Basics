def show_sales_all():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        f.seek(0)
        print(f.read())
    return 0


def show_sales_from(str_number):
    number = int(str_number)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        count = sum(1 for _ in f)
        f.seek(0)
        i = 1
        while i <= count:
            if i >= number:
                print(f.readline())
            else:
                f.readline()
            i += 1
    return 0


def show_sales_from_to(str_number1, str_number2):
    number1 = int(str_number1)
    number2 = int(str_number2)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        count = sum(1 for _ in f)
        f.seek(0)
        i = 1
        while i <= count:
            if number1 <= i <= number2:
                print(f.readline())
            else:
                f.readline()
            i += 1
    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        exit(show_sales_from_to(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 2:
        exit(show_sales_from(sys.argv[1]))
    elif len(sys.argv) == 1:
        exit(show_sales_all())
