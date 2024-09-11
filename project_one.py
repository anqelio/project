from datetime import datetime, timedelta
try:
   birthday_potter = datetime.strptime('2024-7-31','%Y-%m-%d')
   day_today = datetime.now()
   if birthday_potter == day_today:
       print('С днём рождения, Гарри! Вечеринка сегодня!')
   elif day_today < birthday_potter:
       print(f'Вечеринка ещё впереди. Осталось дней {birthday_potter - day_today} до дня рождения Гарри.')
   elif day_today > birthday_potter:
       print(f'Вечеринка уже прошла. До следующего дня рождения Гарри осталось {365 - (day_today - birthday_potter).days} дней')
except ValueError as e:
    print('Некорректный ввод даты')