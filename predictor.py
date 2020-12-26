import pandas as pd
import numpy as np

from hparams import favorite_heroes
from conversion.hero_dictionary import dictionary

reference_table = pd.read_csv('conversion/reference_table.csv')

enemy_team = ['enigma', 
              'dusa', 
              'phoenix', 
              'storm', 
              'wind']
for i in range(len(enemy_team)):
    enemy_team[i] = input("Enter the enemy hero: ")

decision_table = np.zeros((len(enemy_team), reference_table.shape[1] - 1))

i = 0
j = 0
for enemy in enemy_team:
    box = np.zeros((1, len(favorite_heroes) + 1))
    for hero in dictionary:
        for hero_name in hero:
            if enemy == hero_name:
                enemy = hero[0]
                box = reference_table[reference_table['Hero']==enemy].to_numpy()
    decision_table[i, :] = box[:, 1:]
    i+=1
    j+=1

decision_table = np.append(decision_table,
                           [np.sum(decision_table, axis = 0)], axis = 0)

enemy_team.append('Delta')
result = pd.DataFrame(np.transpose(decision_table),
                      index = favorite_heroes, columns = enemy_team)
result = result.sort_values(by = ['Delta'])
print(result.head(5))