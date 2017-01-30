import os.path
import read_web_page
import write_to_csv
import get_scripts_list

data_location = "C:/data/html/"
actions = set()
scripts_list = get_scripts_list.get_scripts_list()
for f in os.listdir(data_location):
    full_file_path = os.path.join(data_location, f)
    number = str(full_file_path).split('-')[1].split('.')[0]
    if os.path.isfile(full_file_path):
        with open(full_file_path, 'r') as html_file:
            (recommendations, manual_updates) = read_web_page.get_recmd_data(html_file.read(), scripts_list)
            if len(recommendations) > 0:
                write_to_csv.write_to_csv('C:/data/processed/recs.csv', recommendations)
            if len(manual_updates) > 0:
                write_to_csv.write_to_csv('C:/data/processed/manual.csv', manual_updates)
            html_file.close()