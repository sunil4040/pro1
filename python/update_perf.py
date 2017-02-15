import time
import date_utils
import get_data_from_csv

recs = get_data_from_csv.get_recs()
bhav_cons = get_data_from_csv.get_bhav_cons()
today_date = time.strftime('%d-%b-%Y').upper()
today_date = date_utils.get_business_day(today_date)
bhav_cons_today = bhav_cons.loc[bhav_cons.TIMESTAMP == today_date]
recs['LATEST_PRICE'] = 0.0
recs['PERF_TO_DATE'] = 0.0
for i, rec in recs.iterrows():
    latest_price = float("{0:.2f}".format(((bhav_cons_today.loc[bhav_cons_today.SYMBOL == rec.SYMBOL]).VWAP).iloc[0]))
    perf_to_date = float("{0:.2f}".format((float(latest_price) - float(rec.PRICE_ON_REC_DATE)) / float(rec.PRICE_ON_REC_DATE) * 100))
    recs.set_value(i, 'LATEST_PRICE', latest_price)
    recs.set_value(i, 'PERF_TO_DATE', perf_to_date)
columns = ['ACTION', 'COMPANY_NAME', 'SYMBOL', 'TARGET', 'RECOMMENDER', 'REC_DATE',
           'DATE_ON_MC', 'PRICE_ON_REC_DATE', 'LATEST_PRICE', 'PERF_TO_DATE', 'URL']
recs = recs[columns]
recs.to_csv('C:/data/processed/recs-perf.csv', sep=';', index=False, quotechar='|')