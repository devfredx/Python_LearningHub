import datetime

now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today)

specific_date = datetime.date(2026, 1, 12)
print(specific_date)

specific_time = datetime.time(20, 30, 45)
print(specific_time)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)

print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))

date_string = "12 January, 2026"
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)

past_date = now - datetime.timedelta(weeks=2)
print(past_date)

diff = tomorrow - now
print(diff.total_seconds())

timestamp = datetime.datetime.timestamp(now)
print(timestamp)

from_ts = datetime.datetime.fromtimestamp(timestamp)
print(from_ts)

print(now.weekday())
print(now.isocalendar())

iso_format = datetime.date.fromisoformat('2026-05-20')
print(iso_format)