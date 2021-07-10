def type_logger(func):
    def wrapper(arg1, arg2):
        return f'{func.__name__}({arg1}: {type(arg1)}, {arg2}: {type(arg2)}), result {func(arg1, arg2)}: {type(func(arg1, arg2))}'
    return wrapper

@type_logger
def calc_cube(x, y):
    return x ** y

arguments = [3, 7.5, 4.8, 6, 2]

for i in arguments:
    print(calc_cube(i, 2))
