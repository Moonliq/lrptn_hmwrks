from datetime import date, datetime, timedelta
dt_now = datetime.now()
print(f'Сегодня {dt_now.strftime("%d.%m.%Y")}')

delta = timedelta(days=1)
dt_now = dt_now - delta
print(f'Вчера {dt_now.strftime("%d.%m.%Y")}')

dt_now = datetime.now()
delta = timedelta(days=30)
dt_now = dt_now - delta
print(f'30 дней назад {dt_now.strftime("%d.%m.%Y")}')

date_string = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt.strftime("%d.%m.%Y %H:%M:%S.%f"))