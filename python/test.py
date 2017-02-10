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

import sys

print (len(sys.argv))
print (sys.argv[0])