"""
In this section we will explore a subset of Python's date time capabilities
Using https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
for reference
"""
from datetime import datetime, timedelta
# crate datetime
print(datetime.now())
print(datetime.utcnow())

# time delta and time math
an_hour_from_now = datetime.now() + timedelta(hours=1)
print(f'An hour from now is {an_hour_from_now}')
# replace elements to look at start and end of periods
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
print(f'Current hour is {current_hour}')
# parse
day_start = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
day_end = day_start + timedelta(days=1, seconds = -1)
print(f"Day start {day_start}, day end {day_end}")

check_date = datetime.now() + timedelta(hours=36)
print(f"{check_date} is {'' if check_date<=day_end and check_date >= day_start else 'NOT'} today")

# print
print("== Date Format ==")
print(check_date.strftime("%m/%d/%Y %H:%M:%S"))
print(check_date.strftime("%b %d %Y"))

#parse
# from dateutil.parser import parse
# test_date = parse("March 05 10:25PM")
# print(test_date)
# test_date = parse("11/11/2011 23:50")

# # timezone and localization, possibly try replacing TZ with LA tz and look at the time
# from pytz import timezone