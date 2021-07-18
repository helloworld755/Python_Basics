class ZeroDiv(Exception):
   pass

try:
   val = int(input('Введите делитель: '))
   if val == 0:
       raise ZeroDiv('Деление на ноль')
except ZeroDiv as e:
  print(e)
else:
    num = 100/val
    print('Деление состоялось,', num)
