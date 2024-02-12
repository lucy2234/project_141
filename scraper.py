from bs4 import BeautifulSoup
import requests
import pandas as pd

url_path="https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&diff=prev&oldid=868364536"
page=requests.get(url_path)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")
print(star_table)
temp_list=[]
table_row=star_table.find_all("tr")

for tr in table_row:
    tds=tr.find_all('td')

    row=[i.text.rstrip()for i in tds]
    temp_list.append(row)

star_name=[]
star_distance=[]
mass=[]
radius=[]

for i in range (1,len(temp_list)):
    star_name.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])