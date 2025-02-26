from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  

def events(eventname,eventdate):
    d={'event':eventname, 'date':eventdate}
    today=datetime.today()
    time_remaining= f'{eventdate.year-today.year} years, {eventdate.month-today.month} months, {eventdate.day-today.day if eventdate.day == today.day else 0} days, {abs(eventdate.hour -today.hour)} hours, {abs(eventdate.minute - today.minute)} minutes'
    timeremainder_week= f'{eventdate - timedelta(weeks=1)}'
    timeremainder_month= f'{eventdate - relativedelta(months=1)}'
    d['time_remaining']=time_remaining
    d['timeremainder_week']=timeremainder_week
    d['timeremainder_month']=timeremainder_month
    return d
    
eventdate=datetime(2025,3,24)
eventname="interview"
print(events(eventname,eventdate))