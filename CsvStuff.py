"""CSV String and File Generating Module

@author: Jan L. Moffett | janlmoffett@gmail.com

This module contains the following functions:
    * csv_print - Prints a list as a csv string.
    * make_csv_header - takes a list of variable names and returns a csv string
    * make_csv_row - takes a list of data points and returns a csv string
    * make_csv_file - creates a new csv file with a header of variable names
    * add_row_csv_file - adds a row to an existing csv file
"""
  
def csv_print(some_list):
    """Prints a list as a csv string.
    
    Args:
        some_list: A list of any type, will be converted to string.
    """
    
    r = ""
    for i,a in enumerate(some_list):
        if i == len(some_list)-1:
            s = str(a)
            r += (s)
            break
            
        s = str(a)
        r += (s + ",")
        
        
    print(r)

#------------------------------------------------------------------------------

def make_csv_header(var_list):
    """Takes a list of variable names and returns a csv string.
    
    Args:
        var_list: A list of variable names.
        
    Returns:
        A string of variable names separated by commas.
    """
    
    r = ""
    
    for i,s in enumerate(var_list):
        if i == len(var_list)-1:
            r += s
            break
        r += (s + ",")
    
    return r    

#------------------------------------------------------------------------------  
def make_csv_row(data_list):
    """Takes a list of data points and returns a csv string.
    
    Args:
        data_list: A list of data points, will convert any data type to string.
        
    Returns:
        A string of data points separated by commas.
    """
    
    r = ""

    for i,a in enumerate(data_list):
        if i == len(data_list)-1:
            r += str(a)
            break
        r += (str(a) + ",")
        
    return r

#------------------------------------------------------------------------------       

def make_csv_file(file_name, header_string):
    """Creates a new csv file with a header of variable names.
    
    Args: 
        file_name: a string ending in '.csv'
        header_string: a string of variable names separated by commas
    """
    
    file = open(file_name,"w")
    file.write(header_string + "\n")
    file.close()

#------------------------------------------------------------------------------
#this function adds a row of data to an existing csv file       
def add_row_csv_file(file_name, csv_row_string):
    """Adds a row to an existing csv file.
    
    Args:
        file_name: a string ending in '.csv'
        csv_row_string: a string of datapoints separated by commas
    """
    
    file = open(file_name,"a")
    file.write(csv_row_string + "\n")
    file.close()
#------------------------------------------------------------------------------   
    
    
def test():
    
    header1 = "Name,Team,Balls,Strikes,Hit,Walk,K"
    name1 = "test060219.csv"
    obs_list1 = ["Cargo","Away","3","1","0","1","0"]
    obs_list2 = ["Bongo","Away","2","2","1","0","0"]
    obs_list3 = ["Jim","Home","0","2","0","0","1"]
    
    make_csv_file(name1, header1)
    csv_row1 = csv_string(obs_list1)
    csv_row2 = csv_string(obs_list2)
    csv_row3 = csv_string(obs_list3)
    add_row_csv_file(name1,csv_row1)
    add_row_csv_file(name1,csv_row2)
    add_row_csv_file(name1,csv_row3)
   
    
