import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

brainFrame = pd.read_csv('brainsize.txt', delimiter='\t')

menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

# Ячейка для кода № 6
menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])

plt.xlabel('PIQ, FSIQ, VIQ')
plt.ylabel('MRI')

plt.show()

# %matplotlib inline