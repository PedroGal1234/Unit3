#Pedro Gallino
#9/29/17
#fir13.py - tells when the next firday the 13th will be for the next 10 years

from datetime import date
from calendar import weekday

year = date.today().year
month = date.today().month 
date = date.today().day 

while True:
    if weekday(year,month,13)