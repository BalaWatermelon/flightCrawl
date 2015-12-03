import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver

dates = ['2016-01-17','2016-01-18','2016-01-19']
driver = webdriver.Firefox()
print "Peach"
for day in dates:
    driver.get('https://book.flypeach.com/default.aspx?ao=B2CZHTW&ori=TPE&des=KIX&dep='+day+'&adt=2&chd=0&inf=0&langculture=zh-TW&bLFF=false')
    time.sleep(4)
    data = BeautifulSoup(driver.page_source,"html.parser")
    print day
    for ele in data.find_all("tr",class_=re.compile("FlightInformation")):
        print ele.select("a")[0].text
        print ele.select(".Deptflight")[0].text.replace('\t',"").replace('\n',"").replace(' ',"")
        print ele.select(".Arrivflight")[0].text.replace('\t',"").replace('\n',"").replace(' ',"")
        print ele.select("label")[0].text.replace('\t',"").replace('\n',"").replace(' ',"")
        print  ele.select("label")[1].text.replace('\t',"").replace('\n',"").replace(' ',"")
        print "=================="

driver.close()
