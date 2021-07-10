def val_checker(x):
    def decor(func):
        def wrapper(*args, **kwargs):
            if x(*args):
                result = func(*args, **kwargs)
                return result
            else:
                raise ValueError
        return wrapper
    return decor


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube(-5))
