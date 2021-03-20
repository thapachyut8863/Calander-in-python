import calendar
import datetime
import time

print(calendar.weekheader(5))
print()

print(calendar.month(2010,3))
print()

print(calendar.firstweekday())
print()

print(calendar.monthcalendar(2020,6))
print()

print(calendar.calendar(2020))
print()

weeK_of_The_day = calendar.weekday(2020,6,14)
print(weeK_of_The_day)

is_leap_year= is_leap_year = calendar.isleap(2021)
print(is_leap_year)


how_many_leaps_day = calendar.leapdays(2020,3000)
print(how_many_leaps_day)