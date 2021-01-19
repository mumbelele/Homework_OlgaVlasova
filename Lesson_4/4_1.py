# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
print('Расчет заработной платы сотрудника')
def salary(productivity, rate, bonus):

    try:
        result = float(productivity) * float(rate) + float(bonus)
        return print(f'Зарплата сотрудника составит {result} у.е.')
    except ValueError as e:
        print(f'Недопустимый тип данных: {e}')
        return print(f'Зарплата сотрудника: ', float('nan'))

try:
    _, productivity, rate, bonus, *_ = argv
except ValueError as e:
    print(f'Недостаточное количество аргументов:{e}')
    print('Необходимо указать выработку в часах, ставку в час и размер премии')
else:
    func_result = salary(productivity, rate, bonus)
