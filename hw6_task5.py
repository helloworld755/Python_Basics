import sys


def user_hobby(argv):
    program, file1, file2, file3 = argv
    with open(str(file1), 'r', encoding='utf-8') as f_1:
        line = f_1.readline()
        names = []
        while line:
            line = line.strip()
            names.append(line)
            line = f_1.readline()

    with open(str(file2), 'r', encoding='utf-8') as f_2:
        line = f_2.readline()
        hobby = []
        while line:
            line = line.strip()
            hobby.append(line)
            line = f_2.readline()

    with open(str(file3), 'w', encoding='utf-8') as f_3:
        i = 0
        while i < len(names):
            if i >= len(hobby):
                f_3.write(f'{names[i]}: None\n')
            else:
                f_3.write(f'{names[i]}: {hobby[i]}\n')
            i += 1
    return 0


exit(user_hobby(sys.argv))
