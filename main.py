import requests
from bs4 import BeautifulSoup
import re
import openpyxl as xl
excel = xl.Workbook()
sheet = excel.active
sheet.title = "rotten tomatoes movies"
sheet.append(["name","year"])
try:

    req = requests.get("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=6")
    soup = BeautifulSoup(req.content, "html.parser")
    rar = soup.find_all("a",class_="js-tile-link")
#print(rar)
    for i in rar:
        dick = i.find("span",class_="p--small").text
        v=i.find('span',class_="smaller").text
        x = v.replace("\r","").replace("\n","")
        w = dick.replace("\r","").replace("\n","")
        name= re.sub("\W"," ",w)
        year = re.sub("\W"," ",x)

        #print(name,year)
        sheet.append([name,year])
except:
    print("error")
excel.save("rotten.xlsx")
