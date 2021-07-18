class NotDigit(ValueError):
    pass

my_list = []
go = True
while go:
    num = input('Введите число: ')
    if num.isdigit():
        my_list.append(int(num))
    elif not num.isdigit():
        try:
            if num == 'stop':
                go = False
                print(my_list)
            else:
                raise NotDigit('Ошибка: Не число.')
        except NotDigit as e:
            print(e)
