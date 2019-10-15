from bs4 import BeautifulSoup
import soupsieve as sv
import pandas as pd

# put all html files you want to extract data from into "target_files"
target_files = ["Github tutorial 0 - 08-October-2019--11.20.html"]
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []

# extracts urls from a target css selector
def get_url(sv_target, targetlist, soup):
    key_tags1 = sv.select(sv_target, soup)
    outputlist = []
    for link in key_tags1:
        targetlist.append(link.get("href"))

# extracts strings from a target css selector
def get_text(sv_target, targetlist, soup):
    key_tags2 = sv.select(sv_target, soup)
    for tag2 in key_tags2:
        targetlist.append(tag2.text)

#writes data to differen columns in a pandas dataframe, which is converted then to a csv
def write_to_excel(filename, col1name, col2name=None, col3name=None, col4name=None, col5name=None, col6name=None):
    df1 = pd.DataFrame({col1name: column1, col2name: column2})
    df1.to_csv(filename, mode="a", index=False, encoding="utf-8-sig")
        
#runs "gets" on each file in target_files, saves to a csv with write_to_excel
def get_all_data():
    for thing in target_files:
        openedfile = open(thing)
        soup = BeautifulSoup(openedfile, "html.parser")
        #insert "get_text"(s) and "get_url"(s) below, they run on every html file in list "target_files"
        #example: get_text("title
        get_text("td.titleColumn > a", column1, soup)
        get_text("td.ratingColumn > strong", column2, soup)
        openedfile.close()
    write_to_excel("test.csv", "Titles", "Ratings")

get_all_data()
