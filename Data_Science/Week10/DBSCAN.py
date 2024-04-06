import matplotlib.pyplot as plt
from sklearn import cluster
from collections import Counter
import pandas as pd

data = pd.read_csv('Mall_Customers.csv')
print(data)

X = data[['Annual Income (k$)','Spending Score (1-100)']]

model = cluster.DBSCAN(eps=10,min_samples=3)
predictor = model.fit_predict(X)

cluster_count = Counter(predictor)
print(cluster_count)

plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=predictor)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('DBSCAN Clustering')
plt.show()