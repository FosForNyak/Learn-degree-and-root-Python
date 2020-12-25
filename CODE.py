import math

print('Choose your language')
print('EN - English')
print('RU - Русский')
o = input('Enter=')

if o == 'RU': # Русский язык
    print('Найти квадратный корень или степень числа')
    l = float(input('Введите число, из которого будет найдено его корень/степень =')) # l - Число, из которого будем находить степень/корень
    print('k - Степень', 's - Корень')
    c = input('Выберите что именно будем узнавать=') # Тут сам выбор, чего мы будем узнавать
    if c == 's':
        print('Результат =', math.sqrt(l), 'Корень вашего числа!')  # Тут логично узнаем корень
    elif c == 'k':
        print('Результат =', math.exp(l), 'Степень вашего числа!') # А тут, так же логично узнаем степень
    else:
        print('Ошибка :/') # Если c не ровно s или k, выдает ошибку
elif o == 'EN': # English lang
    print('Find the square root or power of a number')
    l = float(input('Enter the number from which its root / power will be found =')) # l - The number from which we will find the degree / root
    print('k - Power', 's - Root')
    c = input('Choose what exactly we will learn=') # Here is the choice, what we will learn
    if c == 's':
        print('Result =', math.sqrt(l), 'The root of your number!') # Here we logically find out the root
    elif c == 'k':
        print('Result =', math.exp(l), 'The power of your number!') # And here, we also logically find out the degree
    else:
        print('Error :/')
