import requests
import json
import pandas as pd
import csv

with open("Chuk.csv","w",newline='') as f:
    with open("ID.csv","r") as file:
        c=csv.reader(file)
        h=next(c)
        writer=csv.writer(f)
        writer.writerow([h[0],"Jokes"])
        for row in c:
            a=row[0]
            url="http://api.icndb.com/jokes/"+a
            r=requests.get(url)
            j=json.loads(r.content)
            writer.writerow([a,j['value']['joke']])
            ##print("j['value']['joke']"])
            
           
f.close()