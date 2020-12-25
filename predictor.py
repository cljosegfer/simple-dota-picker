import pandas as pd
import numpy as np

from favorite_heroes import formal_names

reference_table = pd.read_csv('reference_table.csv')

enemy_team = ['Enigma', 
              'Medusa', 
              'Phoenix', 
              'Storm Spirit', 
              'Windranger']
for i in range(len(enemy_team)):
    enemy_team[i] = input("Enter the enemy hero: ")

decision_table = np.zeros((len(enemy_team), reference_table.shape[1] - 1))

i = 0
j = 0
for enemy in enemy_team:
    for hero in reference_table['Hero']:
        if enemy == hero:
            box = reference_table[reference_table['Hero']==enemy].to_numpy()
    decision_table[i, :] = box[:, 1:]
    i+=1
    j+=1

total = np.zeros(reference_table.shape[1] - 1)
for line in range(len(total)):
    total[line] = np.sum(decision_table[:,line])

total = pd.DataFrame(total, index=formal_names, columns=['Delta'])
total = total.sort_values(by = ['Delta'])
print(total.head(3))