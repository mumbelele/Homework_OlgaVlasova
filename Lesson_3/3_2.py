# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
name = input('Enter your name : ')
surname = input('Enter your surname : ')
year = int(input('Enter your birth year : '))
city = input('Enter your city : ')
email = input('Enter your email : ')
telephone = input('Enter your telephone number :')

def my_func (arg_name, arg_surname, arg_year, arg_city, arg_email, arg_phone):
    return f"Your name - {arg_name}, surname - {arg_surname}, birth year- {arg_year}, your city- {arg_city}, your email-  {arg_email}, your telephone number - {arg_phone}"

print(my_func (arg_name=name, arg_surname=surname, arg_year=year, arg_city=city, arg_email=email, arg_phone=telephone))