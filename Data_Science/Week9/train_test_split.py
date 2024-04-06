import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings('ignore', 'X does not have valid feature names')

df = pd.read_csv('brazil-stadium.csv')
# print(pd.isnull(df))
# print(pd.isnull(df).sum())

data_Encoder = LabelEncoder()

df['Stadium_Name'] = data_Encoder.fit_transform(df['Stadium_Name'])
df['Locality'] = data_Encoder.fit_transform(df['Locality'])
df['Federative_Units'] = data_Encoder.fit_transform(df['Federative_Units'])
df['Owner'] = data_Encoder.fit_transform(df['Owner'])
df['Capacity'] = data_Encoder.fit_transform(df['Capacity'])

dt = DecisionTreeClassifier()
dt.fit(df[['Stadium_Name', 'Locality', 'Federative_Units', 'Owner']], df[['Capacity']])
# print(dt.predict([[130, 128, 25, 1]]))

# plot_tree(dt)
# plt.show()

X = df[['Stadium_Name', 'Locality', 'Federative_Units', 'Owner']]
y = df['Capacity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
# print(X_train)

modal = GaussianNB()
modal.fit(X_train, y_train)
print(modal.score(X_test, y_test))
