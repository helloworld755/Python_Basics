'''Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
# первые кавычки
while i < len(my_list):
    if my_list[i].isdigit():
        my_list[i] = f'{int(my_list[i]):02d}'
        my_list.insert(i+1, '"')
    if my_list[i].find('+') != -1:
        my_list[i] = my_list[i].replace('+', '')  # удаление плюса
        # Проверка на числовое значение
        if my_list[i].isdigit():
            my_list[i] = f'+{int(my_list[i]):02d}'  # форматирование и добавление плюса
            my_list.insert(i + 1, '"')
    i += 1

# вторые кавычки
i = len(my_list) - 1
while i >= 0:
    if my_list[i].isdigit():
        my_list.insert(i, '"')
    if my_list[i].find('+') != -1:
        my_list[i] = my_list[i].replace('+', '')  # удаление плюса
        # Проверка на числовое значение
        if my_list[i].isdigit():
            my_list[i] = f'+{int(my_list[i]):02d}'  # форматирование и добавление плюса
            my_list.insert(i, '"')
    i -= 1

print(my_list)

#склеивание строки
message = ''
i = 0
while i < len(my_list):
    message += my_list[i]
    if my_list[i] == '"' and my_list[i+1].isascii():
        message += ''
    elif my_list[i].isascii() and my_list[i+1] == '"':
        message += ''
    else:
        message += ' '
    i += 1

print(message)
