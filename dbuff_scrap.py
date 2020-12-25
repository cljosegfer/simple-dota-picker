import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from favorite_heroes import adress, formal_names

for i in range(len(adress)):
    url = adress[i]
    page = requests.get(url, headers={'user-agent': 'Mozilla/84.0.1'})
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    table = soup('table')[3]
    data = pd.read_html(str(table))[0]
    data.columns = ['n0', 'hero', 'delta', 'n3', 'n4']
    data = data.drop(columns=['n0', 'n3', 'n4'])
    data.loc[len(data) + 1] = [formal_names[i], '0.00%']
    data = data.sort_values(by = ['hero'], ignore_index=True)
    
    if (i == 0):
        reference_table = pd.DataFrame(data)
        reference_table.columns = ['Hero', formal_names[i]]
    else:
        reference_table.insert(i + 1, formal_names[i], data['delta'])

time.sleep(1)

def p2f(x):
    return float(x.strip('%'))

dim = reference_table.shape
for j in range(dim[1])[1:]:
    for i in range(dim[0]):
        delta = reference_table.loc[i, formal_names[j - 1]]
        delta = p2f(delta)
        reference_table.loc[i, formal_names[j - 1]] = delta

reference_table.to_csv('reference_table.csv', index = False)