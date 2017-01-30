get_scrip_list <- function()
{
  scrip_list <- read.csv('C:/data/config/EQUITY_L.csv', header = TRUE, sep = ',', dec = '.')
  return (scrip_list)
}
