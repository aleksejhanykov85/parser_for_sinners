from bs4 import BeautifulSoup
from time import sleep

import pandas as pd
import requests

data = []

# quantity_of_page = int(input("Введите количество страниц: "))

# for page in range(1,quantity_of_page+1):
    
url = "https://sinners.studio/ru/about/"
response = requests.get(url)
sleep(2)
soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.find_all('li', class_="team-member")

for element in elements:
    about = element.find('p').text
    name = about.split(' —')[0]
    post = about.split(' —')[1]
    img = element.get('data-src')
    data.append([name,post,img])

header = ['name','post','img']

df = pd.DataFrame(data, columns=header)
df.to_csv(r'C:\Users\user\Desktop\sinners\about_data.csv', sep=';', encoding='UTF-8-sig')
