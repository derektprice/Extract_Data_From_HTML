from bs4 import BeautifulSoup
import soupsieve as sv
import pandas as pd
import chardet

target_files = ["FILES"]
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

def find_encoding(filename):
    readfile = open(filename, 'rb').read()
    result = chardet.detect(readfile)
    charenc = result['encoding']
    return charenc

def get_all_data():
    loops = 0
    for thing in target_files:
        loops +=1
        print(loops)
        myencoding = find_encoding(thing)
        openedfile = open(thing, encoding=myencoding)
        soup = BeautifulSoup(openedfile, "html.parser")
        get_text("div > h1", column1, soup) #title
        #additional things you want in additional columns
        openedfile.close()
    write_to_excel("NAME OF CSV.csv")

def write_to_excel(filename):
    resultsdict = {"Header1": column1, "Header2": column2, "HEader3": column3, "BLANK2": column4, "BLANK3": column5, "BLANK4": column5, "BLANK5": column6}
    df1 = pd.DataFrame.from_dict(resultsdict, orient="index")
    df2 = pd.DataFrame
    df2 = df1.transpose()
    df2.to_csv(filename, mode="a", index=False, encoding="utf-8-sig")

get_all_data()
