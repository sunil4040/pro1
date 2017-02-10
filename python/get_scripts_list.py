import pandas as pd

script_list = pd.DataFrame()

def get_scripts_list():
    column_names = ['SYMBOL', 'NAME_OF_COMPANY', 'SERIES', 'DATE_OF_LISTING', 'PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER',
               'FACE_VALUE']
    scripts_list = pd.read_csv('C:/data/config/EQUITY_L.csv', encoding='cp1252', header=0, names=column_names,
                usecols=['SYMBOL', 'NAME_OF_COMPANY'])
    scripts_list.NAME_OF_COMPANY = scripts_list.NAME_OF_COMPANY.str.upper()
    return scripts_list

def get_script_symbol(scrip, scripts_list):
    symbol = (scripts_list.loc[scripts_list.NAME_OF_COMPANY.str.startswith(scrip.upper())]).SYMBOL
    if len(symbol) == 1:
        return symbol.iloc[0]
    elif len(symbol) == 0:
        symbol = (scripts_list.loc[scripts_list.NAME_OF_COMPANY.str.startswith('THE ' + scrip.upper())]).SYMBOL
        if len(symbol) == 1:
            return symbol.iloc[0]
        return 'NA'
    else:
        return 'NA'
