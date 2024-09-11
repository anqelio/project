from datetime import datetime, timedelta, random
try:
   birthday_student = datetime.strptime(input('Введите дату рождения студента: '),'%Y-%m-%d')
   if birthday_student == datetime.strptime(("1-1-1900"),'%Y-%m-%d') or ((31-12-1949),'%Y-%m-%d'):
       print('1')
   elif birthday_student == datetime.strptime(("1-1-1950"),'%Y-%m-%d') or ((31-12-1999),'%Y-%m-%d'):
       print('2')
   elif birthday_student == datetime.strptime(("1-1-1800"),'%Y-%m-%d') or ((31-12-1849),'%Y-%m-%d'):
       print('3')
   elif birthday_student == datetime.strptime(("1-1-1850"),'%Y-%m-%d') or ((31-12-1899),'%Y-%m-%d'):
       print('4')
   elif birthday_student == datetime.strptime(("1-1-2000"),'%Y-%m-%d') or ((31-12-2049),'%Y-%m-%d'):
       print('5')
   elif birthday_student == datetime.strptime(("1-1-2050"),'%Y-%m-%d') or ((31-12-2099),'%Y-%m-%d'):
       print('6')
   elif print('7') or print('8') or print('9'):
except ValueError as e:
        print('Некорректный ввод даты')