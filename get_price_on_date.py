import pandas as pd

script_list = pd.DataFrame()

def get_bhav_cons():
    column_names = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
                    'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'VWAP']
    scripts_list = pd.read_csv('C:/data/bhav_cons/bhav_cons.csv', encoding='cp1252', header=0, names=column_names,
                usecols=['SYMBOL', 'TIMESTAMP', 'VWAP'])
    return scripts_list

def get_price_for_date(symbol, rec_date, bhav_cons):
    vwap = (bhav_cons.loc[(bhav_cons.SYMBOL == symbol) & (bhav_cons.TIMESTAMP == rec_date)]).VWAP
    if len(vwap) == 1:
        return vwap.iloc[0]
    else:
        return -1