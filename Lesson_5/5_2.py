# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
file = open('test2.txt', 'r')
text = file.read()
print(text + '\n')

file = open('test2.txt', 'r')
text = file.readlines()
print(str(len(text)) + '- строк в тексте.')

file = open('test2.txt', 'r')
text = file.read()
text = text.split()
print(str(len(text)) + '- количество слов.')

file.close()