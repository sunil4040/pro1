extracted_location = "C:/data/extracted"

process_bhav_arvhive <- function(bhav_archive)
{
  if(file.exists(bhav_archive))
  {
    unzip (bhav_archive, exdir = extracted_location)
    extracted_file_name <- paste0(extracted_location, '/', toString(strsplit(basename(bhav_archive), ".zip")))
    bhav <- read.csv(extracted_file_name, header = TRUE, sep = ',', dec = '.')
    if (is.null(bhav$VWAP))
    {
      bhav$X <- NULL
      bhav <- bhav[!is.na(bhav$SERIES), ]
      bhav <- bhav[bhav$SERIES %in% c('EQ', 'BE'), ]
      bhav$VWAP <- round(bhav$TOTTRDVAL / bhav$TOTTRDQTY, digits = 2)
      write.csv(bhav, extracted_file_name, row.names = FALSE, quote = FALSE)
    }
    else
    {
      print ('Archive already processed : ', extracted_file_name)
    }
  }
  else
  {
    print ('File Not Found : ', full_file_path)
  }
}