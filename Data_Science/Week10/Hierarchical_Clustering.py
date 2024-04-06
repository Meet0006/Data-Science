import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

df = pd.read_excel('applications.xlsx')

X = df[['Points', 'Percentage']]

# Perform hierarchical clustering
HC = linkage(X, method='ward')

dendrogram(HC)
plt.show()
