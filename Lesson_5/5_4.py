# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

numerals_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
filename = 'numerals'

try:
       with open('test4.txt', 'r') as f:
        numerals = f.readlines()

        numerals_rus = []
        for element in numerals:
            key, *others = element.split()
            numerals_rus.append(element.replace(key, numerals_dict[key]))

        with open('test4new.txt', 'w') as f:
            f.writelines(numerals_rus)

except FileNotFoundError:
    print(f'\nError: file "{filename}" not found.')
except IOError:
    print('\nError: input-output error.')