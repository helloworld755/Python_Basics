from collections import Counter

my_list = []
ips = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('"', '')
        content = line.split(sep=' ')
        for x in range(4):
            del content[1]
        while len(content) > 3:
            del content[3]
        my_list.append(tuple(content))
        ips.append(content[0])

find_spamer = dict(Counter(ips))
print(find_spamer)

res = {x: y for x, y in filter(lambda x: find_spamer[x[0]] == max(find_spamer.values()), find_spamer.items())}
print(res)
