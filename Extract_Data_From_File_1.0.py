from bs4 import BeautifulSoup
import soupsieve as sv
import pandas as pd

target_files = ["GitHub Guide 0 - 15-October-2019--22.34.html"]
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []

# give soupsieve target, name of list to output to, and soup
def get_url(sv_target, targetlist, soup):
    key_tags1 = sv.select(sv_target, soup)
    for link in key_tags1:
        targetlist.append(link.get("href"))

def get_text(sv_target, targetlist, soup):
    key_tags2 = sv.select(sv_target, soup)
    for tag2 in key_tags2:
        targetlist.append(tag2.text)

def get_all_data():
    for thing in target_files:
        openedfile = open(thing, errors="surrogateescape") #this error parameter made my programs work together
        soup = BeautifulSoup(openedfile, "html.parser")
        get_text("div > h4", column1, soup)
        get_text("div.wrap > h1", column2, soup)
        #additional things you want in additional columns
        openedfile.close()
    write_to_excel("test.csv")

def write_to_excel(filename):
    resultsdict = {"Headers" : column1, "Hello World" : column2, "BLANK1": column3, "BLANK2":column4, "BLANK3":column5, "BLANK4":column5, "BLANK5":column6}
    df1 = pd.DataFrame.from_dict(resultsdict, orient="index")
    df2 = pd.DataFrame
    df2 = df1.transpose()
    df2.to_csv(filename, mode="a", index=False, encoding="utf-8-sig")

get_all_data()
