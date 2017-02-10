import csv
import os.path

def write_to_csv(full_file_path, data_list):

    csv_file_present = os.path.isfile(full_file_path)
    with open(full_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if(csv_file_present == False):
            if('recs.csv' in full_file_path):
                csv_writer.writerow(['ACTION', 'COMPANY_NAME',  'SYMBOL', 'TARGET', 'RECOMMENDER', 'REC_DATE', 'DATE_ON_MC', 'URL'])
            else:
                csv_writer.writerow(['MC_REC_STRING', 'REC_DATE', 'DATE_ON_MC', 'URL'])
        for item in data_list:
            csv_writer.writerow(item)
        csvfile.close()