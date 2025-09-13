from bs4 import BeautifulSoup

import pandas as pd
import requests

data = []
url = 'https://sinners.studio/ru/job/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all('article')

for element in elements:
    job = element.find('h3').text
    about_job = element.find('p', class_='roobert-m trim').find('span', class_='selection-fix').text.replace('\xa0','')
    data.append([job,about_job])
    
header = ['job', 'about_job']

df = pd.DataFrame(data, columns=header)
df.to_csv(r'C:\Users\user\Desktop\sinners\job_data.csv', sep=';', encoding='UTF-8-sig')
