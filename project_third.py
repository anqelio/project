try:
   brave = input('Вы смелый?')
   leader = input('У вас есть лидерские качества?')
   ambitious = input('Вы амбициозный?')
   risk_taker = input('Вы рискуете?')
   smart = input('Вы умный?')
   loves_learning = input('Вы любите учиться?')
   favorite_subject = input('Ваш любимый предмет?')
   if brave == 'True' or leader == 'True' and favorite_subject == 'Защита от Темных Искусств':
       print('Студент зачислен на факультет Гриффиндор')
   elif ambitious == 'True' and risk_taker == 'True' or favorite_subject == 'Зельеварение':
       print('Студент зачислен на факультет Слизерин')
   elif smart == 'True' and loves_learning == 'True' and not favorite_subject == 'История Магии':
       print('Студент зачислен на факультет Когтевран')
   else:
       print('Студент зачислен на факультет Пуффендуй')
except ValueError as e:
    print('Некорректный ввод даты')