update_latest_price <- function(recs, bhav_cons_last_bus_day)
{
  for( rec in recs )
  {
    rec$LAST_PRICE <- bhav_cons_last_bus_day[bhav_cons_last_bus_day$SYMBOL == rec$SYMBOL, ]$VWAP
    rec$PERF_TO_DATE <- (rec$LAST_PRICE - rec$TARGET) / rec$TARGET * 100
  }
}