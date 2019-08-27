# -*- coding: utf-8 -*-
"""
Using Requests to scrape MLB front office directories.

This module requires you to install the Requests library: https://2.python-requests.org/en/master/

At this stage the the module only saves the webpage response to a text file
Not all url's are successful, and there is some variablity in the structure of 
html pages.  Parsing is in the works.  Going to use BeautifulSoup...
"""

import requests
from bs4 import BeautifulSoup
import CsvStuff

def main():
    
    url_frt = 'https://www.mlb.com/'
    url_bck = '/team/front-office'
    
    #bluejays have a different url
    url_bck_bj = '/team/front-office-directory'
    
    #team names as they appear in url's
    ale_names = ['redsox','bluejays','yankees','rays','orioles']
    alc_names = ['twins','whitesox','indians','royals','tigers']
    alw_names = ['astros','rangers','angels','athletics','mariners']
    nle_names = ['mets','phillies','nationals','braves','marlins']
    nlc_names = ['brewers','cubs','cardinals','pirates','reds']
    nlw_names = ['padres','dodgers','giants','dbacks','rockies']
    
    #change back after testing:
    #team_names = ale_names + alc_names + alw_names + nle_names + nlc_names + nlw_names
    
    #p works for cubs, brewers, mets, nationals, marlins, bluejays, astros
    
    #grouping by how the html page for front office directory is constructed
    #type 1: has link to table under an 'a' tag, text of which refers to "Baseball Operations"
    # red sox, yankees, rays, orioles,
    # twins, white sox, indians, royals, tigers,
    # rangers, athletics, mariners
    # phillies, braves,
    # reds, pirates, cardinals, 
    # dodgers, dbacks, padres, giants,
    
    type1_teams = ['redsox','yankees','rays','orioles']
    type1_teams += ['twins','whitesox','indians','royals','tigers']
    type1_teams += ['rangers','athletics','mariners','phillies','braves']
    type1_teams += ['reds','pirates','cardinals','dodgers','dbacks','padres','giants']
    
    is_type1 = True
    
    #initializing csv file to store titles, names, and teams
    CsvStuff.make_csv_file("BaseballOpsRolodex1.csv","Position Title,Name,Organization")
    
    #for each team
    for n in type1_teams:
        
        #getting contents of webpage
        try:
            x = requests.get(url_frt + n + url_bck)
            #print(x.text)
        except:
            print("!!!ERROR: Something went wrong with the request for " + n)
            continue
        else:
            
            #writing to a text file
            #filename = "fo_" + n + ".txt"
            #file = open(filename, "a")
            #file.write(x.text)
            #file.close()
            
            #turn page text into soup
            fo_soup1 = BeautifulSoup(x.text, "html.parser")
            
            
            if is_type1:
                type1_fo(fo_soup1, n)
                
                
    
    
def type1_fo(fo_soup, team_name):
    
    all_a = fo_soup.find_all("a")
    
    for i,a in enumerate(all_a):
        if "Baseball Operations" in str(a.text):
            #print(str(i+1) + ": " + team_name)
            whole_tag = str(a)
            #print("whole_tag: " + whole_tag)
            table_link = whole_tag[whole_tag.find("href")+6:whole_tag.find(">",whole_tag.find("href")+6)-1]
            #print("table_link: " + table_link)
            
            #request a response from table_link
            #getting contents of webpage
            try:
                x = requests.get(table_link)
                #print(x.text)
            except:
                print("!!!ERROR: Something went wrong with a baseball ops table request for " + team_name)
                print("link used: " + table_link)
                continue
            else:
                bo_soup1 = BeautifulSoup(x.text, "html.parser")
                tr_tags = bo_soup1.find_all("tr")
                for tr in tr_tags:
                    td_tags = tr.find_all("td", text = True)
                    data_str = ""
                    for td in td_tags:
                        #print(str(td.text).replace(","," -"),end = ",")
                        data_str += (str(td.text).replace(","," -") + ",")
                    #print(team_name)
                    data_str += (team_name + "\n")
                    CsvStuff.add_row_csv_file("BaseballOpsRolodex1.csv", data_str)
                    
                    
                
    
main()
