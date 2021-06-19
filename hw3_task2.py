'''
Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
'''

def num_translate_adv(word):
    dictionary = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    return dictionary.get(word)

answer = input("Translation EN => RU: ")
if answer[0].isupper():
    answer = answer.lower()
    result = num_translate_adv(answer)
    print(result.capitalize())
else:
    result = num_translate_adv(answer)
    print(result)
