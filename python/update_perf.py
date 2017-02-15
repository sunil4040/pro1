import time
import datetime
import date_utils
import get_data_from_csv
import get_from_bhav_cons

recs = get_data_from_csv.get_recs()
bhav_cons = get_data_from_csv.get_bhav_cons()
last_bhav_cons_date = time.strftime('%Y-%m-%d')
hour_now = int(time.strftime('%H'))
if (hour_now < 15):
    last_bhav_cons_date = (datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
else:
    last_bhav_cons_date = date_utils.get_business_day(last_bhav_cons_date)
bhav_cons_today = bhav_cons.loc[bhav_cons.TIMESTAMP == last_bhav_cons_date]
recs['LATEST_PRICE'] = 0.0
recs['PERF_TO_DATE'] = 0.0
recs['TARGET_ACHIEVED'] = ''
recs['ACHIEVED_DATE'] = ''
recs['ACHIEVED_IN_DAYS'] = ''
recs['BEST_PRICE_TO_DATE'] = 0.0
recs['BEST_PERF'] = 0.0
recs['BEST_PERF_ACHIEVED_DATE'] = ''
for i, rec in recs.iterrows():
    latest_price = float("{0:.2f}".format(((bhav_cons_today.loc[bhav_cons_today.SYMBOL == rec.SYMBOL]).VWAP).iloc[0]))
    perf_to_date = float("{0:.2f}".format((float(latest_price) - float(rec.PRICE_ON_REC_DATE)) / float(rec.PRICE_ON_REC_DATE) * 100))
    recs.set_value(i, 'LATEST_PRICE', latest_price)
    recs.set_value(i, 'PERF_TO_DATE', perf_to_date)
    (target_achieved, max_price_to_date, max_price_date, max_perf, target_achieved_date, target_achieved_in_days) = \
        get_from_bhav_cons.get_target_info(rec.SYMBOL, rec.TARGET, rec.PRICE_ON_REC_DATE, rec.REC_DATE, bhav_cons)
    recs.set_value(i, 'TARGET_ACHIEVED', target_achieved)
    recs.set_value(i, 'ACHIEVED_DATE', target_achieved_date)
    recs.set_value(i, 'ACHIEVED_IN_DAYS', target_achieved_in_days)
    recs.set_value(i, 'BEST_PRICE_TO_DATE', max_price_to_date)
    recs.set_value(i, 'BEST_PERF', max_perf)
    recs.set_value(i, 'BEST_PERF_ACHIEVED_DATE', max_price_date)
    print (i)

columns = ['ACTION', 'COMPANY_NAME', 'SYMBOL', 'TARGET', 'RECOMMENDER', 'REC_DATE', 'DATE_ON_MC', 'PRICE_ON_REC_DATE',
           'TARGET_ACHIEVED', 'ACHIEVED_DATE', 'ACHIEVED_IN_DAYS', 'BEST_PRICE_TO_DATE', 'BEST_PERF',
           'BEST_PERF_ACHIEVED_DATE', 'LATEST_PRICE', 'PERF_TO_DATE', 'URL']
recs = recs[columns]
recs.to_csv('C:/data/processed/recs-perf.csv', sep=';', index=False, quotechar='|')
# recs = recs.drop('URL', axis = 1)