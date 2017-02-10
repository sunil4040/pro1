# source("add_vwap.R")
# 
# extracted_file_name = 'cm09JAN2017bhav.csv'
# extracted_location = "C:/data/extracted"
# bhav_archive_location = "C:/data/archive/"
# bhav_archive = paste0(bhav_archive_location, extracted_file_name, ".zip")
# unzip (bhav_archive, exdir = extracted_location)
# 
# extracted_file_path = paste0(extracted_location, '/', extracted_file_name)
# add_vwap(extracted_file_path)
# 
# #bhav <- read.csv(full_file_path, header = TRUE, sep = ',', dec = '.')
# #bhav$VWAP <- format(round(bhav$VWAP, 2), nsmall = 2)
# #write.csv(bhav, full_file_path, row.names = FALSE, quote = FALSE)
# 
# # source("get_scrip_list.R")
# # scrip_list <- get_scrip_list()
# 
# files = list.files(bhav_archive_location, full.names = TRUE)
# 
source("add_vwap.R")
bhav_archive_location = "C:/data/archive/"
zip_files = list.files(bhav_archive_location, full.names = TRUE)
sapply(zip_files, FUN = process_bhav_arvhive)


source("process_bhav_archives.R")
process_bhav_archives()

download.file('https://www.nseindia.com/content/historical/EQUITIES/2017/JAN/cm30JAN2017bhav.csv.zip', destfile = 'C:/data/archive/cm30JAN2017bhav.csv.zip', method="libcurl")

source("date_utils.R")

download_for_month('JAN', 2017)

library(dplyr)
recs <- read.csv('C:/data/processed/recs.csv', header = TRUE, sep = ';', dec = '.', quote = '|')
recs_not_na <- recs[!is.na(recs$SCRIP), ]
recs_counts <- recs_not_na %>% group_by(SCRIP) %>% summarize(count=n())

# Testing to setup
get_scrpits_list('NSE')