# from datetime import date
# from datetime import datetime
# from datetime import time
#
# resultDT = dir(datetime)
# resultD = dir(date)
# resultT = dir(time)
#
# print(resultDT)
# print(resultD)
# print(resultT)
from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
# simdi = datetime.today()
#
# result = datetime.now()
# result = simdi.year
# result = simdi.month
# result = simdi.day
# result = simdi.hour
# result = simdi.minute
# result = simdi.second
# result = datetime.ctime(simdi)
#
# result = datetime.strftime(simdi, '%Y')
# result = datetime.strftime(simdi, '%X')
# result = datetime.strftime(simdi, '%d')
# result = datetime.strftime(simdi, '%A')
# result = datetime.strftime(simdi, '%B')
# result = datetime.strftime(simdi, '%Y %B %A')

t = '24 June 2024 hour 22:37:45'

result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1982, 3, 4, 12, 30, 23)

result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)

result = datetime.fromtimestamp(0)

result = simdi - birthday  # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes=10)

result = simdi - timedelta(days=10)

print(result)
