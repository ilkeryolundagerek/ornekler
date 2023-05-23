import requests as req
from bs4 import BeautifulSoup as bs
from models import EarthquakeModel
import pandas as pd

url = 'http://www.koeri.boun.edu.tr/scripts/lst5.asp'
res = req.get(url)
content = bs(res.content, 'lxml').pre.text

lines = content.splitlines()[7:-1]
print(len(lines))
eqs = []
for line in lines:
    line = line.replace('-.-', '0.0')
    eq = EarthquakeModel(line.split())
    eqs.append(eq.__dict__)
df = pd.DataFrame(eqs)
print(df.head())
df.info()
print(df[["latitude","longitude","depth","MD","ML","Mw"]].describe())
print(df.describe(include="O"))