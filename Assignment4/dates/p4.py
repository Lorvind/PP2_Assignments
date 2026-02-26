import datetime

date_format = "%Y.%m.%d"

date1 = datetime.datetime.strptime(input(), date_format)
date2 = datetime.datetime.strptime(input(), date_format)

differnce = (date2 - date1).total_seconds()

print(differnce)