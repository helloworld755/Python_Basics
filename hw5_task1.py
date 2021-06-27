def odd_nums(n):
    for i in range(0, n + 1):
        if i % 2 != 0:
            yield i

odd_to_15 = odd_nums(15)
print(*odd_to_15)
