months_vasya = input().split()
months_dasha = input().split()
bad_weather = input().split()
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
selected_months = []
for month in months:
    if month in months_vasya and month in months_dasha and month not in bad_weather:
        selected_months.append(month)
print(', '.join(selected_months))
