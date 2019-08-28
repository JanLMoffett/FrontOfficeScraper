# FrontOfficeScraper

### Python code to gather names and titles from MLB front office directories online.
 
If you're looking for a job in a Major League Baseball front office like I am, you may want to learn about the people currently working for teams and what their jobs entail.  A good way to start is to compile a list of names and titles from each organization, most of which are available on official MLB team pages.

[FrontOffice2.py](../master/FrontOffice2.py) - _Iterates through front office directory url's and outputs a csv file containing position titles, names from Baseball Operations tables._

This code imports [requests](https://2.python-requests.org/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and [CsvStuff](../master/CsvStuff.py).

[BaseballOpsRolodex2.csv](../master/BaseballOpsRolodex2.csv) - _Output of FrontOffice2.py._

[CsvStuff.py](../master/CsvStuff.py) - _Module of functions to open and append to csv files._

[CleanRolodex.R](../master/CleanRolodex.R) - _R code to clean output of FrontOffice._

[BaseballOpsRolodex3.csv](../master/BaseballOpsRolodex3.csv) - _Output of CleanRolodex.R.  This is the final version of the output - not perfect, but the remaining problems are manageable enough to fix in Excel.  This dataset is meant to be the basis for a contact list with emails, phone numbers, notes, etc._

