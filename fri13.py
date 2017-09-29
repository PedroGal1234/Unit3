#Pedro Gallino
#9/29/17
#fir13.py - tells when the next firday the 13th will be for the next 10 years

from datetime import date
from calendar import weekday

year = date.today().year
month = date.today().month 
date = date.today().day 
repeats = 0
i = 0

while True:
    if weekday(year,month+i,13) == 4:
        print(month,'/',13,'/',year)
        repeats = repeats + 1
    if month == 12:
        month = 0
        year = year +1
    month = month + 1
    if repeats == 10:
        break
    