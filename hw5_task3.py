def generator(list_a, list_b):
    for i in range(0, len(list_a)):
        if i <= len(list_b) - 1:
            yield (list_a[i], list_b[i])
        else:
            yield (list_a[i], None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б']
# classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = generator(tutors, classes)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) #- здесь уже StopIteration
