# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать
# пустая строка.file_user = open('test.txt', 'w')

while True:
    text = input('Введите данные: ')
    if not text:
        break
    file_user.writelines(text + '\n')

file_user.close()