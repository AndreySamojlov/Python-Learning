from datetime import datetime, timedelta
now = datetime.now()
print(f"Сегодня: {now}")
print(f"Вчера: {now-timedelta(days=1)}")
print(f"Месяц назад: {now-timedelta(days=31)}")
str_date = "01/01/17 12:10:03.234567"
ran_date = datetime.strptime(str_date, "%d/%m/%y %H:%M:%S.%f")
print(ran_date)