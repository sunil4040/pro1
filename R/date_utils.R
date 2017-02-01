is_business_day <- function(date)
{
  holidays <- read.csv('C:/data/config/HolidayList.csv')
  formatted_date <- format(date, "%d-%b-%Y")
  day <- format(date, '%a')
  if((formatted_date %in% holidays) || (day %in% c('Sat', 'Sun')))
  {
    return (FALSE)
  }
  else
  {
    return (TRUE)
  }
}

get_archive_name <- function(date)
{
  day <- format(date, '%d')
  month <- toupper(format(date, '%b'))
  year <- format(date, '%Y')
  file_name <- paste0('cm', day, month, year, '.csv.zip')
  return (file_name)
}

get_bhav_archive_url <- function(date)
{
  # URL Example - https://www.nseindia.com/content/historical/EQUITIES/2017/JAN/cm30JAN2017bhav.csv.zip
  month <- toupper(format(date, '%b'))
  year <- format(date, '%Y')
  full_url <- paste0('https://www.nseindia.com/content/historical/EQUITIES/', year, '/', month, '/', get_archive_name(date_today))
  return (full_url)
}