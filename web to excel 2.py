from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.nfl.com/standings/league/2020/reg/'
page= requests.get(url)
soup=BeautifulSoup(page.text,'lxml')

table=soup.find('table',{'summary':'Standings - Detailed View'})
headers=[]
for i in table.find_all('th'):
    title=i.text.strip()
    headers.append(title)

df= pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    data=row.find_all('td')
    row_data =[td.text.strip() for td in data]
    length = len(df)
    df.loc[length]=row_data

df.to_csv('result1.csv')
