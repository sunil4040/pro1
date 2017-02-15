# # import read_web_page
# #
# # read_web_page.get_recmd_data("C:\\data\\html\\ResearchReports-39.html")
# #
# # import write_to_csv
# # data_list = []
# # data_list.append([1, 'Test', 'Write', 'to', 'csv'])
# # data_list.append([2, 'Test', 'Write', 'to', 'csv'])
# # write_to_csv.write_to_csv('C:/data/test.csv', data_list)
#
# import get_scripts_list
# import pandas as pd
#
# scripts = get_scripts_list.get_scripts_list()
# symbol = (((scripts.loc[scripts.NAME_OF_COMPANY.str.startswith('Adani Trans')]).SYMBOL))
# if len(symbol) == 1:
#     print ((symbol.iloc[0]))
# else:
#     print ('NA')

# import datetime
#
# date_string = '2015 research report'
# try:
#     datetime_object = datetime.datetime.strptime(date_string, '%B %d, %Y')
#     print (datetime_object)
# except ValueError:
#     print (date_string, 'Exception occured')

# import sys
#
# print (len(sys.argv))
# print (sys.argv[0])

# import get_price_on_date
# import datetime
#
# bhav_cons = get_price_on_date.get_bhav_cons()
# try:
#     datetime_object = datetime.datetime.strptime('December 29, 2016', '%B %d, %Y')
#     date_string = (datetime_object.strftime('%d-%b-%Y')).upper()
# except:
#     print('Failed to convert date')
# print (get_price_on_date.get_price_for_date('ITC', date_string, bhav_cons))

# import requests
# html = requests.get('http://www.moneycontrol.com/news/broker-research-reports-13-1-next-0.html')
# print (html.content)

# import date_utils
# print(date_utils.get_business_day('15-NOV-2016'))

# import re
#
# print(re.findall('(\d+)', 'Rs.600'))

# import pandas as pd
# import datetime
#
# holidays = pd.read_csv('C:/data/config/HolidayList.csv', encoding='cp1252', header=0, names=['DATE'])
# for day_date in holidays.DATE:
#     datetime_object = datetime.datetime.strptime(day_date, '%d-%b-%Y')
#     date_string = (datetime_object.strftime('%Y-%m-%d'))
#     print(date_string)

# import date_utils
# print (date_utils.get_business_day('2017-01-26'))
# print (date_utils.get_number_of_business_days('2017-01-20', '2017-01-27'))

# import time
# print (int(time.strftime('%H')))

import datetime
print ((datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d'))