import datetime

today = datetime.date.today()
today -= datetime.timedelta(days=5)

print(today)