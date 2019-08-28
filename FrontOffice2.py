# -*- coding: utf-8 -*-
"""
Using Requests to scrape MLB front office directories and output csv files.

This module requires requests, BeautifulSoup, and CsvStuff
"""

import requests
from bs4 import BeautifulSoup
import CsvStuff

def main():
    
    url_frt = 'https://www.mlb.com/'
    url_bck = '/team/front-office'
    
    #bluejays have a different url
    #url_bck_bj = '/team/front-office-directory'
    
    #team names as they appear in url's
    #ale_names = ['redsox','bluejays','yankees','rays','orioles']
    #alc_names = ['twins','whitesox','indians','royals','tigers']
    #alw_names = ['astros','rangers','angels','athletics','mariners']
    #nle_names = ['mets','phillies','nationals','braves','marlins']
    #nlc_names = ['brewers','cubs','cardinals','pirates','reds']
    #nlw_names = ['padres','dodgers','giants','dbacks','rockies']
    
    #grouping team names by how the html page for front office directory is constructed
    
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
    
    #type2: has table containing names on first page, not in separate token table
    #p works for cubs, brewers, mets, nationals, marlins, bluejays, astros
    type2_teams = ['bluejays','astros','mets','nationals','marlins','brewers','cubs']
    #type2_types = ['t2']*len(type2_teams) #for testing
    
    #lists to hold team names and types
    team_names = type1_teams + type2_teams
    team_types = ['t1']*len(type1_teams) + ['t2']*len(type2_teams)
    
    #initializing csv file to store titles, names, and teams
    CsvStuff.make_csv_file("BaseballOpsRolodex2.csv","Position Title,Name,Organization")
    
    #for each team
    for i,n in enumerate(team_names): #change input back to team_names
        #front office directory url
        fod_url = url_frt + n + url_bck
        #bluejays have a different url
        if n == "bluejays":
            fod_url += '-directory'
        
        #getting contents of webpage
        try:
            x = requests.get(fod_url)
            #print(x.text)
        except:
            print("!!!ERROR: Something went wrong with the request for " + n)
            print("attempted url: " + fod_url)
            continue
        else:
            #writing to a text file
            #filename = "fo_" + n + ".txt"
            #file = open(filename, "a")
            #file.write(x.text)
            #file.close()
            
            #turn page text into soup
            fo_soup1 = BeautifulSoup(x.text, "html.parser")
            
            #call functions depending on type
            if team_types[i] == 't1': #change back to team_types[i]
                type1_fo(fo_soup1, n)
                
            elif team_types[i] == 't2': #change back to team_types[i]
                type2_fo(fo_soup1, n)
                
            else:
                print("!!!Error: Unknown team type for " + n)
    
    
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
                    CsvStuff.add_row_csv_file("BaseballOpsRolodex2.csv", data_str)
                    
def type2_fo(fo_soup, team_name):  
    all_p = fo_soup.find_all("p")   

    for i,p in enumerate(all_p):
        str_p = str(p)
        str_p = str_p.replace(",","")
        str_p = str_p.replace("&amp;","and")
        str_p = str_p.replace("<br/>",("," + team_name + "\n"))
        str_p = str_p.replace("</b>"," ")         
        str_p = str_p.replace("<b>","")   
        str_p = str_p.replace("<span>","")
        str_p = str_p.replace("</span>","")
        str_p = str_p.replace("<p>","")
        str_p = str_p.replace("</p>","")
        
        if ("Baseball Operations" in str_p) or ("Scouting" in str_p) or ("Research" in str_p) or ("Development" in str_p) or ("Data" in str_p):
            
            data_str = str_p + "," + team_name
            CsvStuff.add_row_csv_file("BaseballOpsRolodex2.csv", data_str)
    
main()

    