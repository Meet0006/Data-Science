import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

df = pd.read_excel('applications.xlsx')

X = df[['Points', 'Percentage']]
k_means = KMeans(n_clusters=3)
k_means.fit(X)

df['Cluster'] = k_means.labels_

print(k_means.predict([[500, 81]]))

plt.scatter(df['Points'], df['Percentage'], c=df['Cluster'])
plt.xlabel('Points')
plt.ylabel('Percentage')
plt.grid(True)
plt.title('K-means Clustering')
plt.show()
