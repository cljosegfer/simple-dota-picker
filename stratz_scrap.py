from selenium import webdriver
import time
import pandas as pd

from hparams import bracketIds, timeIds, regionIds, gameModeIds
from dota_stats import HERO_BY_ID

url = ('https://stratz.com/heroes/meta/trends?' +
       'bracketIds=' + bracketIds +
       '&time=' + timeIds +
       '&regionIds=' + regionIds +
       '&gameModeIds=' + gameModeIds)

driver = webdriver.Firefox(executable_path = '/home/jose/.local/share/gecko_driver/geckodriver')
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(30)

data = []
for hero in range(3, 123):
    xpath = "/html/body/div[2]/main/div[2]/div[3]/div[" + str(hero) + "]/a"
    element = driver.find_element_by_xpath(xpath)
    hero_link = element.get_attribute('href')
    hero_id = hero_link.strip('https://stratz.com/heroes/')
    pr_xpath = xpath + "/div[13]"
    element = driver.find_element_by_xpath(pr_xpath)
    pr = element.text
    data.append([hero_id, pr])    
driver.quit()

pickrate_table = pd.DataFrame(data, columns=('Hero', 'Pick Rate'))
i = 0
for heroId in pickrate_table.loc[:,'Hero']:
    for word in HERO_BY_ID.items():
        if int(heroId) == word[0]:
            pickrate_table.loc[i,'Hero'] = word[1]
    i += 1

def p2f(x):
    return float(x.strip('%'))

dim = pickrate_table.shape
for i in range(dim[0]):
    prate = pickrate_table.loc[i, 'Pick Rate']
    prate = p2f(prate)
    pickrate_table.loc[i, 'Pick Rate'] = prate
pickrate_table = pickrate_table.sort_values(by = ['Hero'], ignore_index=True)
pickrate_table.to_csv('pickrate_table.csv', index = False)