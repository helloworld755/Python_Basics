'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы.
'''

def thesaurus(*args):
    dictionary = {}
    i = 0
    while i < len(args):
        name = args[i]
        first_letter = name[0]
        dictionary.setdefault(first_letter, [])
        dictionary[first_letter].append(name)
        i += 1
    return dictionary

result = thesaurus("Иван", "Мария", "Петр", "Илья")
print(result)