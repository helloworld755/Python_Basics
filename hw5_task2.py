n = 15 # или сделать input
odd_nums = (i for i in range(1, n + 1) if i % 2 != 0)
for i in odd_nums:
    print(i)
