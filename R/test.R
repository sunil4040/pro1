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
recs_not_na <- recs[!is.na(recs$SYMBOL), ]
recs_counts <- recs_not_na %>% group_by(SYMBOL) %>% summarize(count=n())

# Testing to setup
get_scrpits_list('NSE')

recs_perf <- read.csv('C:/data/processed/recs-perf.csv', header = TRUE, sep = ';', dec = '.', quote = '|')
recs_wo_url <- recs_perf[,-17]
recs_wo_url[recs_wo_url$TARGET_ACHIEVED == 'Yes', ]
recs_best_perf_not_na <- recs_wo_url[!is.na(recs_wo_url$BEST_PERF), ]
recs_best_perf_not_na[with(recs_best_perf_not_na, order(-BEST_PERF)), ]
aggregate(PERF_TO_DATE ~ RECOMMENDER, recs_wo_url[grepl('2017$', recs_wo_url$REC_DATE), ], max)
buy_recs <- recs_wo_url[recs_wo_url$ACTION %in% c('BUY', 'HOLD', 'ACCUMULATE'), ]
targets_achieved <- buy_recs %>% group_by(RECOMMENDER, TARGET_ACHIEVED) %>% summarise(count=length(TARGET_ACHIEVED))
recommenders <- aggregate(TARGET_ACHIEVED ~ RECOMMENDER, buy_recs, length)

recommenders$noise_count <- sapply(recommenders$RECOMMENDER, function(x) if(nrow(targets_achieved[targets_achieved$TARGET_ACHIEVED == 'NOISE' & targets_achieved$RECOMMENDER == x, ])==0) 0 else targets_achieved[targets_achieved$TARGET_ACHIEVED == 'NOISE' & targets_achieved$RECOMMENDER == x, ]$count)

recs_best_perf_not_na <- recs_wo_url[!is.na(recs_wo_url$BEST_PERF), ]
recs_best_perf_not_na[with(recs_best_perf_not_na, order(-BEST_PERF)), ]