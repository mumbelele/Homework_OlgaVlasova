# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

try:
    with open('test5.txt', 'w') as f:
        f.write(' '.join([str(randint(0, 100)) for i in range(randint(2, 100))]))

    with open('test5.txt') as f:
        try:
            array = [int(n) for n in f.readline().split()]
            print(array)
            print(f'Сумма: {sum(array)}')
        except ValueError:
            print('Incorrect value')

except IOError:
    print('\nIO error.')