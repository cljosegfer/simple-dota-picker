import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from hparams import favorite_heroes, patch
from hero_dictionary import dictionary

adress = []
for hero in favorite_heroes:
    for hero_element in dictionary:
        if hero == hero_element[0]:
                adress.append('https://www.dotabuff.com/heroes/' + 
                              hero_element[1] + '/counters?date=patch_' + patch)


for i in range(len(adress)):
    url = adress[i]
    page = requests.get(url, headers={'user-agent': 'Mozilla/84.0.1'})
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    table = soup('table')[3]
    data = pd.read_html(str(table))[0]
    data.columns = ['n0', 'hero', 'delta', 'n3', 'n4']
    data = data.drop(columns=['n0', 'n3', 'n4'])
    data.loc[len(data) + 1] = [favorite_heroes[i], '0.00%']
    data = data.sort_values(by = ['hero'], ignore_index=True)
    
    if (i == 0):
        reference_table = pd.DataFrame(data)
        reference_table.columns = ['Hero', favorite_heroes[i]]
    else:
        reference_table.insert(i + 1, favorite_heroes[i], data['delta'])
    time.sleep(1)
    print("Reading", favorite_heroes[i], "data,", i + 1, "/", len(adress))


def p2f(x):
    return float(x.strip('%'))

dim = reference_table.shape
for j in range(dim[1])[1:]:
    for i in range(dim[0]):
        delta = reference_table.loc[i, favorite_heroes[j - 1]]
        delta = p2f(delta)
        reference_table.loc[i, favorite_heroes[j - 1]] = delta

reference_table.to_csv('reference_table.csv', index = False)