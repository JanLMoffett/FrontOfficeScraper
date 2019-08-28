
#set working directory
setwd('C:/Users/Jan/Desktop/MLB/FrontOfficeScraper/FrontOfficeScraper/')

#using stringr for string operations
library(stringr)

#reading in dataset output by FrontOfficeScraper
d <- read.csv('BaseballOpsRolodex2.csv', stringsAsFactors = F)

#team names as they appear in url's
ale_names = c('redsox','bluejays','yankees','rays','orioles')
alc_names = c('twins','whitesox','indians','royals','tigers')
alw_names = c('astros','rangers','angels','athletics','mariners')
nle_names = c('mets','phillies','nationals','braves','marlins')
nlc_names = c('brewers','cubs','cardinals','pirates','reds')
nlw_names = c('padres','dodgers','giants','dbacks','rockies')
#vector of all 30 team names
team_names = c(ale_names, alc_names, alw_names, nle_names, nlc_names, nlw_names)

#vector to hold indices of rows that need to be deleted from df
delete_rows <- vector(length = 0)

d2 <- data.frame("PositionTitle" = d$Position.Title,
                 "Name" = d$Name,
                 "Organization" = d$Organization,
                 stringsAsFactors = F)


for(i in seq_along(d2[[1]])){
  #if row is team name alone, put on delete list
  if(d2$PositionTitle[i] %in% team_names){
    delete_rows <- append(delete_rows, i)  
  }  
  
}

#delete empty rows from df
d3 <- d2[-delete_rows,]

#compile list of rows that need PositionTitle entry split into PositionTitle and Name
fix_rows <- vector(length = 0)

#iterate through each row
for(i in seq_along(d3[[1]])){
  #if team name appears in Name column and Organization column is empty
  if(d3$Name[i] %in% team_names & d3$Organization[i] == ""){
    #copy Name entry over to Organization column
    d3$Organization[i] <- d3$Name[i]
    #add index to fix_rows vector
    fix_rows <- append(fix_rows, i)
  
  }
  
} 
#iterate through rows that need to be fixed
d3_fix <- d3[fix_rows,]
for(i in seq_along(d3_fix[[1]])){
  ts <- d3_fix[i,1]  
  #separate position from name and enter into correct columns
  #different rules for different teams
  #for bluejays, names are before ': ' and titles are after ': '
  if(d3_fix$Organization[i] == "bluejays"){
    sep = ":  "
    ts_split <- str_split(ts, sep)
    nm <- ts_split[[1]][1]
    pt <- ts_split[[1]][2]
    
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
  }
  
  #for astros, names are after '|'
  if(d3_fix$Organization[i] == "astros"){
    sep = " | "
    ts_split <- strsplit(ts, sep, fixed = T)
    pt <- ts_split[[1]][1]
    nm <- ts_split[[1]][2]
    
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
  }
  
  #for mets, nationals, and marlins names are after ': '
  if(d3_fix$Organization[i] == "mets"){
    sep = ": "
    ts_split <- str_split(ts, sep)
    pt <- ts_split[[1]][1]
    nm <- ts_split[[1]][2]
    
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
    
  }
  if(d3_fix$Organization[i] == "nationals"){
    sep = ": "
    ts_split <- str_split(ts, sep)
    pt <- ts_split[[1]][1]
    nm <- ts_split[[1]][2]
    
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
    
  }
  if(d3_fix$Organization[i] == "marlins"){
    #sep = ": "
    #ts_split <- strsplit(ts, sep, fixed = T, useBytes = T)
    #pt <- ts_split[[1]][1]
    #nm <- ts_split[[1]][2]
    
    #d3_fix[i,1] <- pt
    #d3_fix[i,2] <- nm
    
  }
  
  #the brewers need to be divided by the second to last space
  if(d3_fix$Organization[i] == "brewers"){
    
    
    spaces <- str_locate_all(ts, " ")
    sec_to_last <- spaces[[1]][length(spaces[[1]][,1])-1,1]
    
    pt <- str_sub(ts, start = 1, end = sec_to_last-1)
    nm <- str_sub(ts, start =  sec_to_last+1, end = nchar(ts))
    
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
  }
  
  #the cubs are divided by " - "
  if(d3_fix$Organization[i] == "cubs"){
    sep = " - "
    ts_split <- str_split(ts,sep)
    pt <- ts_split[[1]][1] 
    nm <- ts_split[[1]][2] 
    d3_fix[i,1] <- pt
    d3_fix[i,2] <- nm
  }
  
}

#concat fixed rows back onto df
d4 <- rbind(d3[-fix_rows,],d3_fix)

# PositionTitles and Names Need to be switched for the rays, dbacks and indians
switch_rows <- which(d4$Organization == "rays" | d4$Organization == "dbacks" | d4$Organization == "indians")
d4_switch <- d4[switch_rows,]
for(i in seq_along(d4_switch[[1]])){
  pt <- d4_switch[i,2]
  d4_switch[i,2] <- d4_switch[i,1]
  d4_switch[i,1] <- pt
}

#concat switched rows back onto df
d5 <- rbind(d4[-switch_rows,],d4_switch)

#writing df to csv file
write.csv(d5, "BaseballOpsRolodex3.csv")






