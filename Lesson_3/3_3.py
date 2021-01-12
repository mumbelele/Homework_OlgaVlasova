# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших
# двух аргументов.
def my_func(arg_1, arg_2, arg_3):
    numbers = [arg_1, arg_2, arg_3]
    sum_num = sum(numbers) - min(numbers)
    return sum_num

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(my_func(a, b, c))