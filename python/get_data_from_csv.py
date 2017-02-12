import pandas as pd
import csv

def get_scripts_list():
    column_names = ['SYMBOL', 'NAME_OF_COMPANY', 'SERIES', 'DATE_OF_LISTING', 'PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER',
               'FACE_VALUE']
    scripts_list = pd.read_csv('C:/data/config/EQUITY_L.csv', encoding='cp1252', header=0, names=column_names,
                usecols=['SYMBOL', 'NAME_OF_COMPANY'])
    scripts_list.NAME_OF_COMPANY = scripts_list.NAME_OF_COMPANY.str.upper()
    return scripts_list


def get_bhav_cons():
    column_names = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
                    'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'VWAP']
    bhav_cons = pd.read_csv('C:/data/bhav_cons/bhav_cons.csv', encoding='cp1252', header=0, names=column_names,
                usecols=['SYMBOL', 'TIMESTAMP', 'VWAP'])
    return bhav_cons


def get_recs():
    column_names = ['ACTION', 'COMPANY_NAME', 'SYMBOL', 'TARGET', 'RECOMMENDER',
                    'REC_DATE', 'DATE_ON_MC', 'PRICE_ON_REC_DATE', 'URL']
    recs = pd.read_csv('C:/data/processed/recs.csv', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                       encoding='cp1252', header=0, names=column_names)
    return recs

