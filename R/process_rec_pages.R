process_rec_pages <- function(end_number)
{
  # http://www.moneycontrol.com/news/broker-research-reports-13-1-next-0.html
  url_prefix <- 'http://www.moneycontrol.com/news/'
  temp_location <- 'C:/data/temp/'
  pages_range <- seq(0, 9)
  number <- 0
  for (i in pages_range)
  {
    for (j in pages_range)
    {
      number <- (i*10 + j + 1)
      file_name <- paste0('broker-research-reports-13-', number, '-next-', i, '.html')
      full_url <- paste0(url_prefix, file_name)
      dest_file <- paste0(temp_location, file_name)
      download.file(url = full_url, destfile = dest_file, method="libcurl")
      command <- paste0('python C:/Users/sanas/PycharmProjects/ProcessRecs/launch.py ', temp_location)
      system(command, intern = FALSE, ignore.stdout = TRUE, ignore.stderr = FALSE, wait = TRUE)
      file.remove(dest_file)
      if(end_number == number)
        break
    }
    if(end_number == number)
      break
  }
}