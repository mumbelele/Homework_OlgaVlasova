# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                           Физика:   30(л)   —   10(лаб)
#                      Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('test6.txt', 'r', encoding='utf-8') as les_file:
    content = les_file.readlines()
    for_result_dict = []

    for lesson in content:

        symbols = [el for el in lesson]
        for_result_dict.append(''.join(symbols[0:symbols.index(':')]))
        d = []
        for digit in symbols:  # находим числа
            if digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                d.append(digit)
            elif digit == '(':
                d.append(' ')
        digit_list = ''.join(d).split()
        total_hours = 0
        for c in digit_list:
            total_hours += int(c)

        for_result_dict.append(total_hours)

        result_dict = dict(for_result_dict[i:i+2] for i in range(0, len(for_result_dict), 2))
    print(result_dict)