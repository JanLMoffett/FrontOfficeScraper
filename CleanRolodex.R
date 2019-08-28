
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

#iterate through each row
for(i in seq_along(d2[[1]])){
  
  #if row is team name alone, put on delete list
  if(d2$PositionTitle[i] %in% team_names){
    delete_rows <- append(delete_rows, i)  
  }
  
  #if the team is the rays, indians, dbacks, 
  # Name and PositionTitle entries need to be switched
  if(d2$Organization[i] == 'rays' | d2$Organization[i] == 'indians' | 
     d2$Organization[i] == 'dbacks'){
  tmp_name <- d2$PositionTitle[i]
  d2$PositionTitle[i] <- d2$Name[i]
  d2$Name[i] <- tmp_name
    
  }
  
  #if team name appears in Name column and Organization col empty
  if(d2$Name[i] %in% team_names & d2$Organization[i] == ""){
    #copy Name entry over to Organization column
    d2$Organization[i] <- d2$Name[i]
    
    #separate position from name and enter into correct columns
    #different rules for different teams
    
    if(d2$Name[i] == 'bluejays'){
      #for bluejays, names are before ': ' and titles are after ': '
      tmp_str <- d2$PositionTitle[i]
      bef_aft <- str_split(tmp_str,': ',2)
      d2$Name[i] <- bef_aft[1]
      d2$PositionTitle[i] <- bef_aft[2]
      
    }else if(d2$Name[i] == 'astros'){
      #for astros, names are after '|'
      tmp_str <- d2$PositionTitle[i]
      bef_aft <- str_split(tmp_str,"|",2)
      d2$Name[i] <- bef_aft[2]
      d2$PositionTitle[i] <- bef_aft[1]
      
    }else if(d2$Name[i] == 'mets' | d2$Name[i] == 'nationals' | d2$Name[i] == 'marlins'){
      #for mets, nationals, and marlins names are after ': '
      tmp_str <- d2$PositionTitle[i]
      bef_aft <- str_split(tmp_str,': ',2)
      d2$Name[i] <- bef_aft[2]
      d2$PositionTitle[i] <- bef_aft[1]
    }
    
  #deal with url's in name or title
  }
  
    
}
warnings()
#delete rows in delete list
delete_rows

PositionTitle <- c("President","Fred Willingham","Boris Vignetti")
Name <- c("Bruce Johnson","Vice President","Manager")
Organization <- c("dodgers","indians","rays")
mini_df <- data.frame(PositionTitle, Name, Organization, stringsAsFactors = F)

mini_df
for(i in seq_along(mini_df[[1]])){
#if the team is the rays, indians, dbacks, 
# Name and PositionTitle entries need to be switched
  if(mini_df$Organization[i] == 'rays' | mini_df$Organization[i] == 'indians' | 
     mini_df$Organization[i] == 'dbacks'){
    tmp_name <- mini_df$PositionTitle[i]
    tmp_title <- mini_df$Name[i]
    
    mini_df$PositionTitle[i] <- tmp_title
    mini_df$Name[i] <- tmp_name    
  }
}
  
mini_df


