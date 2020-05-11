# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:39:39 2020

@author: Admin
"""

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(title=title,message=message,app_icon=r"C:\Users\Admin\Desktop\index.ico", timeout=20)
def getData(url):
    r=requests.get(url)
    return r.text
if __name__ == "__main__": 
    while True:
    #notifyMe("Vikas and Vindhya","Lets Bring down this corona virus now")
        myHtmlData=getData("https://www.mohfw.gov.in/")
    
        soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())
        myDatastr=" "
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr+=tr.get_text()
            myDatastr=myDatastr[2:]
            itemList=myDatastr.split("\n\n")
    
        states=['Karnataka','Delhi','Uttarakhand']
        for item in itemList[0:32]:
            dataList=item.split('\n')
            if dataList[1] in states:
            
                print(dataList)
                nTitle='cases of Covid-19'
                nText=f"   State { dataList[1]}\n  Total Confirmed cases: {dataList[2]}\n  Cured/Discharged/Migrated:{dataList[3]}\n  Deaths:{dataList[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(216000)
