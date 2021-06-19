'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого).
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов
в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
'''

import random

def get_jokes(n):
    # объявление исходных массивов слов
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    i = 0
    while i < n:
        text = ""
        # добавление 1 слова
        number = random.randint(0, len(nouns) - 1)
        text = text + nouns[number] + " "
        # добавление 2 слова
        number = random.randint(0, len(adverbs) - 1)
        text = text + adverbs[number] + " "
        # добавление 3 слова
        number = random.randint(0, len(adjectives) - 1)
        text = text + adjectives[number]
        # добавление в массив шуток
        joke_list.append(text)
        i += 1
    return joke_list

def get_jokes_norepeats(n):
    # объявление исходных массивов слов
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    i = 0
    while i < n:
        text = ""
        # добавление 1 слова
        number = random.randint(0, len(nouns) - 1)
        text = text + nouns[number] + " "
        nouns.pop(number) # удаление слова из списка
        # добавление 2 слова
        number = random.randint(0, len(adverbs) - 1)
        text = text + adverbs[number] + " "
        adverbs.pop(number) # удаление слова из списка
        # добавление 3 слова
        number = random.randint(0, len(adjectives) - 1)
        text = text + adjectives[number]
        adjectives.pop(number) # удаление слова из списка
        # добавление в массив шуток
        joke_list.append(text)
        i += 1
    return joke_list

repeats = input("Одно слово в одной шутке - y/n ? ")
if repeats == "y":
    answer = int(input("Введите количество шуток (до 5): "))
    if answer > 5:
        answer = 5
    print(get_jokes_norepeats(answer))
else:
    answer = int(input("Введите количество шуток: "))
    print(get_jokes(answer))
