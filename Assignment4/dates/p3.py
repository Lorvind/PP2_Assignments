import datetime

today = datetime.datetime.now()

print(today)

today = today.replace(microsecond=0)

print(today)