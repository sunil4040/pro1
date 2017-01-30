source("add_vwap.R")

process_bhav_archives <- function()
{
  bhav_archive_location <- "C:/data/archive/"
  zip_files <- list.files(bhav_archive_location, full.names = TRUE)
  sapply(zip_files, FUN = process_bhav_arvhive)
}