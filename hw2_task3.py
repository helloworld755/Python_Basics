'''Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

message = ''
i = 0
while i < len(my_list):
    if my_list[i].isascii():
        if my_list[i].isdigit():
            message += '"'
            message += f'{int(my_list[i]):02d}'
            message += '" '
        if my_list[i].find('+') != -1:
            my_list[i] = my_list[i].replace('+', '')
            if my_list[i].isdigit():
                message += '"+'
                message += f'{int(my_list[i]):02d}'
                message += '" '
    else:
        message += my_list[i]
        message += ' '
    i += 1

print(message)
