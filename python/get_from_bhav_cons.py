import date_utils

def get_price_for_date(symbol, rec_date, bhav_cons):
    business_day = date_utils.get_business_day(rec_date)
    vwap = (bhav_cons.loc[(bhav_cons.SYMBOL == symbol) & (bhav_cons.TIMESTAMP == business_day)]).VWAP
    if len(vwap) == 1:
        return vwap.iloc[0]
    else:
        return -1

def get_target_info(symbol, target, price_on_rec_date, rec_date, bhav_cons):
    if(target <= (price_on_rec_date * 1.02)):
        return ('NOISE', None, None, None, None, None)
    bhav_cons_symbol = bhav_cons.loc[bhav_cons.SYMBOL == symbol]
    data_from_rec_date = bhav_cons_symbol.loc[bhav_cons_symbol.TIMESTAMP > rec_date]
    max_price_rec = data_from_rec_date.loc[data_from_rec_date['VWAP'].idxmax()]
    max_perf = float("{0:.2f}".format((max_price_rec.VWAP - price_on_rec_date) / price_on_rec_date * 100))
    if max_price_rec.VWAP < target:
        return ('No', max_price_rec.VWAP, max_price_rec.TIMESTAMP, max_perf, None, None)
    else:
        target_achieved_date = (data_from_rec_date.loc[data_from_rec_date.VWAP >= target]).TIMESTAMP.min()
        target_achieved_in_days = date_utils.get_number_of_business_days(rec_date, target_achieved_date)
        return ('Yes', max_price_rec.VWAP, max_price_rec.TIMESTAMP, max_perf, target_achieved_date, target_achieved_in_days)
