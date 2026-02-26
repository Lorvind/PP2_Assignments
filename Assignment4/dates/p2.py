import datetime

today = datetime.date.today()

delta = datetime.timedelta(days=1)
yesterday = today - delta
tomorrow = today + delta

print(yesterday, today, tomorrow, sep='\n')