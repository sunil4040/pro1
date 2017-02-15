process_bhav_archives <- function()
{
  start_time <- Sys.time()
  print (start_time)
  if(file.exists('C:/data/bhav_cons/bhav_cons.csv'))
  {
    file.remove('C:/data/bhav_cons/bhav_cons.csv')
  }
  bhav_archive_location <- "C:/data/archive/"
  zip_files <- list.files(bhav_archive_location, pattern = "*.csv.zip", full.names = TRUE)
  sapply(zip_files, FUN = process_bhav_arvhive)
  end_time <- Sys.time()
  print (end_time)
  print ('Time taken: ', end_time - start_time)
}