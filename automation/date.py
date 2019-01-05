#!/bin/bash/python3

import datetime,calendar

now=datetime.datetime.now()
print('today\'s day is '+str(now.day))
#print(now.year)

year=now.year
print(year)
day= now.day
print(day)
month=now.month
#totalday = 2

days_in_year=calendar.monthrange()
print(days_in_year)

if year%4==0:
    #totalday==366
    print("it is a leap year")
    #print("percentage of this year completed is "+ str((now.day)/totalday))
else:
    #totalday==365
    print("not a leap year")
    #print("percentage of this year completed is "+ str((now.day)/totalday))
