
remove_tags <- function(a_string){
  
  while(str_detect(a_string, "<") | str_detect(a_string, ">")){
    loc_op <- str_locate(a_string, "<")[1]
    loc_cl <- str_locate(a_string, ">")[1]
    
    if(is.na(loc_op)){
      loc_op <- 1
      
    }
    if(is.na(loc_cl)){
      loc_cl <- nchar(a_string)
      
    }
    
    p <- str_sub(a_string, start = loc_op, end = loc_cl)
    
    if(nchar(p)>0){
    
      a_string <- str_replace(a_string, p, "")
    }
    
    return(a_string)
  }
}