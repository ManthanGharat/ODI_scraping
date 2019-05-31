import requests
from bs4 import BeautifulSoup
import pandas as pd
values=[]
casie=[]
heap=[]
career=[]
title_2=[]
name=[]
year=[]
runs=[]
nat=[]
name1=[]
year1=[]
runs1=[]
heap1=[]
joy=[]
name3=[]
year3=[]
runs3=[]
list4=["https://en.m.wikipedia.org/wiki/List_of_Australia_ODI_cricketers"]
list3=["https://en.m.wikipedia.org/wiki/List_of_India_ODI_cricketers"]
list2=["https://en.wikipedia.org/wiki/List_of_New_Zealand_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_South_Africa_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Sri_Lanka_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_West_Indies_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Bangladesh_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Pakistan_ODI_cricketers"]
links=["https://en.m.wikipedia.org/wiki/List_of_England_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Canada_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Afghanistan_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Ireland_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_United_Arab_Emirates_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Papua_New_Guinea_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Netherlands_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Nepal_ODI_cricketers","https://en.wikipedia.org/wiki/List_of_Scotland_ODI_cricketers"]
#------------------------------------------------------------------------------------------------------------------------------------------------
for a in links:
    r=requests.get(a)
    soup=BeautifulSoup(r.text,"lxml")
    for item in soup.find_all('span',class_='fn'):
        for a in item.find_all('a',href=True):
            jam=a["title"]
            heap.append(jam)
    title=soup.find("caption").text.replace("ODI cricketers\n"," ")
    table=soup.find('table',{"class":"wikitable sortable plainrowheaders"}).tbody
    rows = table.find_all('tr')
    for i in range (1,len(rows)):
        tds = rows[i].find_all('td')
        if len(tds)==0:
             pass
        else:
            values = [" ",tds[1].text,tds[2].text," ",tds[4].text," "," "," "," ",' ',' ',' ',' ','']
            rome=values[4]
            gin=values[1]
            net=values[2]
            casie.append(rome)
            career.append((gin,net))
            title_2.append(title)
    for a in heap: 
        if len(heap)>len(casie):
                heap.pop(len(heap)-1)         
df=pd.DataFrame()
df["Name"]=heap
df["Nationality"]=title_2
df["Career"]=career
df["Cumulative Runs"]=casie
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
for a in list2:
    r=requests.get(a)
    soup=BeautifulSoup(r.text,"lxml")
    table=soup.table
    table_rows = table.find_all("tr")
    nation=table.find("th").text.replace("ODI cricketers\n"," ")
    for tr in table_rows:
        td=tr.find_all("td")
        rows=[i.text for i in td]
        if len(rows)<=3:
            pass
        else:
            name.append(rows[1])
            year.append(rows[2])
            runs.append(rows[4])
            nat.append(nation)
df1=pd.DataFrame()
df1["Name"]=name
df1["Nationality"]=nat
df1["Career"]=year
df1["Cumulative Runs"]=runs
#----------------------------------------------------------------------------------------------------------------------------------------------------------
for p in list3:
    r=requests.get(p)
    soup=BeautifulSoup(r.text,"lxml")
    table=soup.table
    table=soup.find('table',{"class":"wikitable plainrowheaders sortable"}).tbody
    table_rows = table.find_all("tr")
    for tr in table_rows:
        for jen in tr.find_all("th"):
            for m in jen.find_all("a",href=True):
                jam=m.get("title")
                heap1.append(jam)
    del heap1[0:15]
    del heap1[78]
    del heap1[84]
    del heap1[114]
    del heap1[162]
    del heap1[135]
    del heap1[124]
    del heap1[135]
    del heap1[95]
    for tr in table_rows:
        td=tr.find_all("td")
        rows=[i.text for i in td]
        if len(rows)<=3:
            pass
        else:
            start=rows[1].replace("\n", " ")
            end=rows[2].replace("\n"," ")
            year1.append((start,end))
            runs1.append(rows[4].replace("\n", " "))
           
df2=pd.DataFrame()
df2["Name"]=heap1
df2["Nationality"]="Indian"
df2["Career"]=year1
df2["Cumulative Runs"]=runs1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
for q in list4:
    r=requests.get(q)
    soup=BeautifulSoup(r.text,"lxml")
    table=soup.table
    table=soup.find('table',{"class":"wikitable sortable"}).tbody
    table_rows = table.find_all("tr")
    for tr in table_rows:
        td=tr.find_all("td")
        rows=[i.text for i in td]
        if len(rows)<=3:
            pass
        else:
            name3.append(rows[1])
            year3.append(rows[2])
            runs3.append(rows[4])
df3=pd.DataFrame()
df3["Name"]=name3
df3["Nationality"]="Australian"
df3["Career"]=year3
df3["Cumulative Runs"]=runs3
#------------------------------------------------------------------------------------------------------------------------------------------------
#Merging all the files
df4=df2.append(df)
df5=df4.append(df3)
df6=df5.append(df1)
df6.to_csv("finish.csv")
print("Done")
