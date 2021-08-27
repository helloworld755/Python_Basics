import json

with open('users.csv', 'r', encoding='utf-8') as f_1:
    line = f_1.readline()
    names = []
    while line:
        line = line.strip()
        names.append(line)
        line = f_1.readline()

with open('hobby.csv', 'r', encoding='utf-8') as f_2:
    line = f_2.readline()
    hobby = []
    while line:
        line = line.strip()
        hobby.append(line)
        line = f_2.readline()

my_dict = {}

i = 0
while i < len(names):
    if i >= len(hobby):
        my_dict.setdefault(names[i], None)
    else:
        my_dict.setdefault(names[i], hobby[i])
    i += 1

print(my_dict)

with open('res3.json', 'w', encoding='utf-8') as f_3:
    my_str = json.dumps(my_dict)
    f_3.write(my_str)

with open('res3.json', 'r', encoding='utf-8') as f_3:
    check_str = f_3.read()
    check_dict = json.loads(check_str)
    print(check_dict)
