import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

brainFrame = pd.read_csv('brainsize.txt', delimiter='\t')

menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])

plt.xlabel('PIQ, FSIQ, VIQ')
plt.ylabel('MRI')

plt.show()

# %matplotlib inline