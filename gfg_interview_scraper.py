# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 14:35:49 2016

@author: lakshay.tutlani
"""

import json
from pprint import pprint
import urllib2;
from bs4 import BeautifulSoup; 
#import pdfkit
#import os

def scrap_data(name):
    link="http://www.geeksforgeeks.org/tag/"+name;
    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page)
    
    article_total=soup.find("div", {"id": "main"})
    article_list=article_total.find_all("article");
    link_list=set();
    for i in article_list:
        link=i.find("a")
        link_list.add(link.attrs["href"])
    
    count=0;    
    for i in link_list:
        count=count+1;
        page = urllib2.urlopen(str(i))
        soup = BeautifulSoup(page)
        filename=name+str(count)+".html"
                
        head=soup.find("h1");
        body=soup.find("div",{"class":"entry-content"})
        #content=body.find_all("p")
        #content='\n'.join(map(str, content))
        with open(filename, "a") as f:
            f.write(str(head))
            f.write(str(body))
            #path_wkthmltopdf = r'C:\Users\lakshay.tutlani\Downloads\wkhtmltox-0.12.3.2_msvc2013-win64.exe'
            #config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            #pdfkit.from_file(filename, name+str(count)+".pdf",configuration=config)
            f.close()
            #os.remove(filename)
        
        

data=None;
with open('gfg_config.json') as data_file:    
    data = json.load(data_file)

pprint(data)

for i in data["company"]:
    print(i);
    if len(i['name']) != 0:
        scrap_data(i['name'])
        

