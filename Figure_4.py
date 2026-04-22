import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

brainFrame = pd.read_csv('brainsize.txt', delimiter='\t')

menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

mcorr = menDf.corr(method='pearson', numeric_only=True)

sns.heatmap(mcorr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('корреляционная тепловая карта (мужчины)')

# plt.savefig('attribute_correlations_women.png')
plt.show()