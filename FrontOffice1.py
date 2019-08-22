# -*- coding: utf-8 -*-
"""
Using Requests to scrape MLB front office directories.

This module requires you to install the Requests library: https://2.python-requests.org/en/master/

At this stage the the module only saves the webpage response to a text file
Not all url's are successful, and there is some variablity in the structure of 
html pages.  Parsing is in the works.  Going to use BeautifulSoup...
"""

import requests

def main():
    
    url_frt = 'https://www.mlb.com/'
    url_bck = '/team/front-office/'
    
    #team names as they appear in url's
    ale_names = ['redsox','bluejays','yankees','rays','orioles']
    alc_names = ['twins','whitesox','indians','royals','tigers']
    alw_names = ['astros','rangers','angels','athletics','mariners']
    nle_names = ['mets','phillies','nationals','braves','marlins']
    nlc_names = ['brewers','cubs','cardinals','pirates','reds']
    nlw_names = ['padres','dodgers','giants','diamondbacks','rockies']
    
    team_names = ale_names + alc_names + alw_names + nle_names + nlc_names + nlw_names
    
    #for each team
    for n in team_names:
        
        #getting contents of webpage
        try:
            x = requests.get(url_frt + n + url_bck)
            #print(x.text)
        except:
            print("ERROR: Something went wrong with the request!")
            print(x)
        else:
            
            filename = "fo_" + n + ".txt"
            
            #writing to a text file
            file = open(filename, "a")
            file.write(x.text)
            file.close()
        
    
main()
