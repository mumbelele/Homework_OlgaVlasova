# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

fin_res = 0
e = False
while e != True:
    num = input("Укажите цифры через пробел. Чтобы выйти из цикла введите '/': ").split()
    res = 0
    for el in range(len(num)):
        if num[el] == "/":
            e = True
            break
        else:
            res = res + int(num[el])
    fin_res = fin_res + res
    print(f'Промежуточная сумма: {fin_res}')
print(f'Конец программы, итоговая сумма чисел: {fin_res}')