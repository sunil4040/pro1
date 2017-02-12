import datetime
import pandas as pd

def is_business_day(day_date):
    datetime_object = datetime.datetime.strptime(day_date, '%d-%b-%Y')
    date_string = (datetime_object.strftime('%d-%b-%Y'))
    holidays = pd.read_csv('C:/data/config/HolidayList.csv', encoding='cp1252', header=0, names=['DATE'])
    day = (datetime_object.strftime('%a'))
    weekend = ['Sat', 'Sun']
    temp = (holidays.loc[(holidays.DATE == date_string)]).DATE
    if len(temp) != 0 or day in weekend:
        return False
    return True

def get_business_day(day_date):
    if(is_business_day(day_date)):
        return day_date
    else:
        datetime_object = datetime.datetime.strptime(day_date, '%d-%b-%Y')
        previous_day = datetime_object - datetime.timedelta(days=1)
        date_string = (previous_day.strftime('%d-%b-%Y')).upper()
        return get_business_day(date_string)