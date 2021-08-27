import os
import random

folder = 'some_data'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 2):
   f_name = ''.join(random.sample(letters, random.randint(5, 10)))
   f_content = bytes(random.randint(0, 255)
                     for _ in range(random.randrange(10 ** 5)))
   with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
       f.write(f_content)

size_dict = {100: None, 1000: None, 10000: None, 100000: None}

for key in size_dict:
    my_list = []
    for item in os.scandir(folder):
        if int(key) >= item.stat().st_size > int(key) / 10:
            my_list.append(item.stat().st_size)
    size_dict[key] = len(my_list)

print(size_dict)

