extracted_location = "C:/data/extracted"

process_bhav_arvhive <- function(bhav_archive)
{
  bhav_cons_file <- 'C:/data/bhav_cons/bhav_cons.csv'
  bhav_cons_exists <- file.exists(bhav_cons_file)
  
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
      bhav_cons <- data.frame()
      if(bhav_cons_exists)
      {
        bhav_cons <- read.csv(bhav_cons_file, header = TRUE, sep = ',', dec = '.')
        bhav_cons <- rbind(bhav_cons, bhav)
      }
      else
      {
        bhav_cons <- bhav
        file.create(bhav_cons_file)
      }
      bhav_cons <- unique(bhav_cons)
      write.csv(bhav_cons, bhav_cons_file, row.names = FALSE, quote = FALSE)
    }
    else
    {
      print ('Archive already processed : ', extracted_file_name)
    }
    file.remove(extracted_file_name)
  }
  else
  {
    print ('File Not Found : ', full_file_path)
  }
}