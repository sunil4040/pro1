is_business_day <- function(day_date)
{
  day_date <- as.Date(day_date)
  holidays <- read.csv('C:/data/config/HolidayList.csv')
  formatted_date <- format(day_date, "%d-%b-%Y")
  day <- format(day_date, '%a')
  if((formatted_date %in% holidays$DATE) || (day %in% c('Sat', 'Sun')))
  {
    return (FALSE)
  }
  else
  {
    return (TRUE)
  }
}

get_archive_name <- function(day_date)
{
  day_date <- as.Date(day_date)
  day <- format(day_date, '%d')
  month <- toupper(format(day_date, '%b'))
  year <- format(day_date, '%Y')
  file_name <- paste0('cm', day, month, year, 'bhav.csv.zip')
  return (file_name)
}

get_bhav_archive_url <- function(day_date)
{
  # URL Example - https://www.nseindia.com/content/historical/EQUITIES/2017/JAN/cm02JAN2017bhav.csv.zip
  day_date <- as.Date(day_date)
  if(is_business_day(day_date))
  {
    month <- toupper(format(day_date, '%b'))
    year <- format(day_date, '%Y')
    full_url <- paste0('https://www.nseindia.com/content/historical/EQUITIES/', year, '/', month, '/', get_archive_name(day_date))
    return (full_url)
  }
}

download_for_month <- function(month, year)
{
  today <- Sys.Date()
  require(Hmisc)
  valid_months <- c('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
  month <- toupper(month)
  if(month %in% valid_months)
  {
    month_start_date <- paste0(year, '-', month, '-01')
    number_of_days_in_month <- monthDays(as.Date(month_start_date, "%Y-%b-%d"))
    month_end_date <- paste0(year, '-', month, '-', number_of_days_in_month)
    dates_of_month <- as.character(seq.Date(as.Date(month_start_date, "%Y-%b-%d"), as.Date(month_end_date, "%Y-%b-%d"), 'day'))
    for(date_of_month in dates_of_month)
    {
      if(date_of_month > today)
      {
        break
      }
      if(is_business_day(date_of_month))
      {
        url_for_date <- get_bhav_archive_url(date_of_month)
        archive_name <- get_archive_name(date_of_month)
        file_name_on_disk <- paste0('C:/data/archive/', archive_name)
        download.file(url = url_for_date, destfile = file_name_on_disk, method="libcurl")
      }
    }
  }
  else
  {
    print ('Invalid Month : ', month)
  }
}
