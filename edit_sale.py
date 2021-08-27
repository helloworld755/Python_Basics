def edit_sale(argv):
    program, number, val = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        count = sum(1 for _ in f)
        # список значений
        f.seek(0)
        my_list = []
        i = 0
        while i < count:
            my_list.append(f.readline())
            i += 1
    # меняем значение
    if int(number) <= count:
        my_list[int(number)-1] = val + '\n'
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            f.seek(0)
            i = 0
            while i < count:
                f.write(my_list[i])
                i += 1
    else:
        print('Такого номера строки нет!')
    return 0


if __name__ == '__main__':
    import sys

    exit(edit_sale(sys.argv))
