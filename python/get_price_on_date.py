import date_utils

def get_price_for_date(symbol, rec_date, bhav_cons):
    business_day = date_utils.get_business_day(rec_date)
    vwap = (bhav_cons.loc[(bhav_cons.SYMBOL == symbol) & (bhav_cons.TIMESTAMP == business_day)]).VWAP
    if len(vwap) == 1:
        return vwap.iloc[0]
    else:
        return -1