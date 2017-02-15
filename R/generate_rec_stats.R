generate_rec_stats <- function()
{
  recs_perf <- read.csv('C:/data/processed/recs-perf.csv', header = TRUE, sep = ';', dec = '.', quote = '|')
  recs_wo_url <- recs_perf[,-17]
  rec_stats <- as.data.frame(recs_wo_url %>% group_by(RECOMMENDER) %>% summarise(Total=n()))
  rec_stats$TargetAchieved <- sapply(rec_stats$RECOMMENDER, function(x) if(nrow(recs_wo_url[recs_wo_url$TARGET_ACHIEVED == 'Yes' & recs_wo_url$RECOMMENDER == x, ])==0) 0 else nrow(recs_wo_url[recs_wo_url$TARGET_ACHIEVED == 'Yes' & recs_wo_url$RECOMMENDER == x, ]))
  rec_stats$TargetAchievedPercent <- round(rec_stats$TargetAchieved / rec_stats$Total * 100, 2)
  rec_stats$NOISE <- sapply(rec_stats$RECOMMENDER, function(x) if(nrow(recs_wo_url[recs_wo_url$TARGET_ACHIEVED == 'NOISE' & recs_wo_url$RECOMMENDER == x, ])==0) 0 else nrow(recs_wo_url[recs_wo_url$TARGET_ACHIEVED == 'NOISE' & recs_wo_url$RECOMMENDER == x, ]))
  rec_stats$NOISEPercent <- round(rec_stats$NOISE / rec_stats$Total * 100, 2)
  return (rec_stats)
}