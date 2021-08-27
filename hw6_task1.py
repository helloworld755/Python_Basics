with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_list = []
    for line in f:
        line = line.replace('"', '')
        content = line.split(sep=' ')
        for x in range(4):
            del content[1]
        while len(content) > 3:
            del content[3]
        my_list.append(tuple(content))

for i in my_list:
    print(i)
