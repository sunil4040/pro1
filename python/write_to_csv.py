import csv
import os.path

def write_to_csv(full_file_path, data_list):

    csv_file_present = os.path.isfile(full_file_path)
    with open(full_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if(csv_file_present == False):
            if('recs.csv' in full_file_path):
                csv_writer.writerow(['ACTION', 'COMPANY_NAME',  'SYMBOL', 'TARGET', 'RECOMMENDER',
                                     'REC_DATE', 'DATE_ON_MC', 'PRICE_ON_REC_DATE','URL'])
            else:
                csv_writer.writerow(['MC_REC_STRING', 'REC_DATE', 'DATE_ON_MC', 'URL'])
        for item in data_list:
            csv_writer.writerow(item)
        csvfile.close()

def write_to_csv_perf(full_file_path, data_list):

    with open(full_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['ACTION', 'COMPANY_NAME',  'SYMBOL', 'TARGET', 'RECOMMENDER',
                             'REC_DATE', 'DATE_ON_MC', 'PRICE_ON_REC_DATE', 'LATEST_PRICE',
                             'PERF_TO_DATE', 'URL'])
        for item in data_list:
            csv_writer.writerow(item)
        csvfile.close()