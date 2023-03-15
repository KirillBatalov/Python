months = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
month2check = input()
if month2check in months:
    print('В месяце 31 день.')
elif month2check == 'февраль':
    print('В месяце 28 или 29 дней.')
else:
    print('В месяце 30 дней.')
