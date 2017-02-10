get_scrpits_list <- function(exchange)
{
  if(exchange == 'NSE')
  {
    download.file(url = 'https://www.nseindia.com/content/equities/EQUITY_L.csv', destfile = 'C:/data/config/EQUITY_L.csv', method="libcurl")
    equities_list <- read.csv('C:/data/config/EQUITY_L.csv', header = TRUE, sep = ',', dec = '.')
    equities_list <- equities_list[!is.na(equities_list$SERIES), ]
    equities_list <- equities_list[equities_list$SERIES %in% c('BE', 'EQ'), ]
    equities_list$NAME.OF.COMPANY <- toupper(equities_list$NAME.OF.COMPANY)
    write.csv(equities_list, 'C:/data/config/EQUITY_L.csv', row.names = FALSE, quote = FALSE)
  }
  else if(exchange == 'NSE')
  {
    # Download and process BSE scripts list
  }
}