import datetime
import pandas as pd

def is_business_day(day_date):
    if isinstance(day_date, str):
        day_date = datetime.datetime.strptime(day_date, '%Y-%m-%d')
    day = (day_date.strftime('%a'))
    weekend = ['Sat', 'Sun']
    if day in weekend:
        return False
    date_string = (day_date.strftime('%Y-%m-%d'))
    holidays = pd.read_csv('C:/data/config/HolidayList.csv', encoding='cp1252', header=0, names=['DATE'])
    temp = (holidays.loc[(holidays.DATE == date_string)]).DATE
    if len(temp) != 0:
        return False
    return True

def get_business_day(day_date):
    if isinstance(day_date, str):
        day_date = datetime.datetime.strptime(day_date, '%Y-%m-%d')
    if(is_business_day(day_date)):
        return day_date.strftime('%Y-%m-%d')
    else:
        previous_day = day_date - datetime.timedelta(days=1)
        return get_business_day(previous_day.strftime('%Y-%m-%d'))

def get_number_of_business_days(from_date, to_date):
    no_of_business_days = 0
    if isinstance(from_date, str):
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    if isinstance(to_date, str):
        to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    while(to_date > from_date):
        if(is_business_day(to_date)):
            no_of_business_days = no_of_business_days + 1
        to_date = to_date - datetime.timedelta(days=1)
    return no_of_business_days