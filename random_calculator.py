import pandas as pd
import numpy as np

reference_table = pd.read_csv('conversion/reference_table.csv')
pickrate_table = pd.read_csv('conversion/pickrate_table.csv')
reference = reference_table.to_numpy()
pickrate = pickrate_table.to_numpy()

dim = reference.shape
random = np.zeros(dim[1] - 1)
for i in range(1, dim[1]):
    random[i - 1] = np.sum(np.multiply(pickrate[:, 1], reference[:, i])) / 100

random = np.append('Random', random)
reference = np.vstack((reference, random))

columns = reference_table.columns
reference_table = pd.DataFrame(reference)
reference_table.columns = columns

reference_table.to_csv('conversion/reference_table.csv', index = False)