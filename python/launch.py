import os.path
import sys
import read_web_page
import write_to_csv
import get_data_csv

if len(sys.argv) != 2:
    print('Usage: launch.py <html files input directory>')
    sys.exit(-1)
data_location = sys.argv[1]
if not os.path.isdir(data_location):
    print(data_location, 'is not a valid directory>')
    sys.exit(-1)
scripts_list = get_data_csv.get_scripts_list()
bhav_cons = get_data_csv.get_bhav_cons()
for f in os.listdir(data_location):
    full_file_path = os.path.join(data_location, f)
    number = str(full_file_path).split('-')[1].split('.')[0]
    if os.path.isfile(full_file_path):
        with open(full_file_path, 'r') as html_file:
            (recommendations, manual_updates) = read_web_page.get_recmd_data(html_file.read(), scripts_list, bhav_cons)
            if len(recommendations) > 0:
                write_to_csv.write_to_csv('C:/data/processed/recs.csv', recommendations)
            if len(manual_updates) > 0:
                write_to_csv.write_to_csv('C:/data/processed/manual.csv', manual_updates)
            html_file.close()