import pandas as pd
from sklearn import preprocessing, tree
import warnings
from matplotlib import pyplot as plt
from sklearn.tree import plot_tree

warnings.filterwarnings('ignore', message='X does not have valid feature names')

salary = pd.read_csv('salary.csv')

salary_prepro = preprocessing.LabelEncoder()

company = salary_prepro.fit_transform(salary['company'])
job = salary_prepro.fit_transform(salary['job'])
degree = salary_prepro.fit_transform(salary['degree'])

salary['company'] = company
salary['job'] = job
salary['degree'] = degree

reg = tree.DecisionTreeClassifier()
reg.fit(salary[['company', 'job', 'degree']], salary[['salary_more_then_100k']])
print(reg.predict([[0, 0, 0]]))

plot_tree(reg, feature_names=[0, 1, 0], class_names=['yes', 'no'], filled=True)
plt.show()
