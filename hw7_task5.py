import os
import random
import json

folder = 'some_data'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
exts = ['.txt', '.bin', '.css', '.html', '.py', '.csv']
for _ in range(10 ** 2):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255)
                      for _ in range(random.randrange(10 ** 5)))
    with open(os.path.join(folder, f'{f_name}' + random.choice(exts)), 'wb') as f:
        f.write(f_content)

size_dict = {100: None, 1000: None, 10000: None, 100000: None}

for key in size_dict:
    my_list = []
    for root, dirs, files in os.walk(folder):
        for item in files:
            if int(key) >= os.stat(os.path.join(root, item)).st_size > int(key) / 10:
                filename, file_extension = os.path.splitext((os.path.join(root, item)))
                if len(my_list) == 0:
                    my_list.append(file_extension)
                elif my_list.count(file_extension) == 0:
                    my_list.append(file_extension)
                else:
                    pass
    size_dict[key] = (len(my_list), my_list)

print(size_dict)

with open('some_data\data.json', 'w') as fp:
    json.dump(size_dict, fp)
