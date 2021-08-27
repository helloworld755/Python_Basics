'''
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения
— словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия
начинается с соответствующей буквы.
'''

def thesaurus_adv(*args):
    dictionary = {}
    i = 0
    while i < len(args):
        full_name = args[i].split()
        surname = full_name[1]
        name = full_name[0]
        dictionary.setdefault(surname[0], {})
        dictionary[surname[0]].setdefault(name[0], [])
        minidict = dictionary[surname[0]]
        minidict[name[0]].append(args[i])
        i += 1
    return dictionary

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)
