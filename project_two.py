from datetime import datetime, timedelta
import random
try:
   birthday_student = datetime.strptime(input('Введите дату рождения студента: '),'%Y-%m-%d')
   gender = str(input('Введите пол студента: '))
   ascii_code = str(input('Введите первую букву фамилии: '))
   #1-ая цифра
   if 1900 <= birthday_student.year <= 1949:
       print('1')
   elif 1950 <= birthday_student.year <= 1999:
       print('2')
   elif 1800 <= birthday_student.year <= 1849:
       print('3')
   elif 1850 <= birthday_student.year <= 1899:
       print('4')
   elif 2000 <= birthday_student.year <= 2049:
       print('5')
   elif 2050 <= birthday_student.year <= 2099:
       print('6')
   elif birthday_student.year < 1900 or birthday_student.year > 2099:
        print(random.randint(7, 9))
    #2-ая и 3-ая цифра
   formatted_year = birthday_student.strftime('%y')
   if birthday_student.year == 1900 or 2099:
       print(formatted_year)
    #4-ая и 5-ая цифра
   formatted_month = birthday_student.strftime('%m')
   if birthday_student.month == 1 or 12:
       print(formatted_month)
    #6-ая и 7-ая цифра
   formatted_day = birthday_student.strftime('%d')
   if birthday_student.day == 1 or 31:
       print(formatted_day)
    #8-ая цифра
   if gender == 'Мужской':
       print('1')
   else:
       print('2')
   #9-ая и 10-ая цифра
   print(ord(ascii_code))
except ValueError as e:
        print('Некорректный ввод даты')