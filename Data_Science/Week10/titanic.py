import pandas as pd
import numpy as np
import statistics
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset from above url
df = pd.read_csv('train.csv')

# Fetch data using pandas and print
# print(df)

# Print column wise null value
# print(df.isnull().sum())

# Missing value graph : X axes column names and Y axes count of missing values.
# X = df.columns
# Y = df.isnull().sum()
#
# plt.bar(X, Y)
# plt.xlabel('column names')
# plt.ylabel('count of missing values')
# plt.show()

# print count of survived and not survived passangers list.
#   0 means died , 1 means survived
# For Research : https://www.encyclopedia-titanica.org/
# print('died: ', np.sum(df.Survived == 0), '||', 'survived: ',
#       np.sum(df.Survived == 1))  # we can use others methods like: unique, mask, lamda

# print pie chart of survived vs not survived. ( with percentage )
# total_count = [np.sum(df.Survived == 0), np.sum(df.Survived == 1)]
# plt.pie(total_count, autopct='%.2f%%', labels=['died', 'survived'])
# plt.show()

# print gender wise count of survived and not survived.
# print('Survived Male: ', np.sum((df.Sex == 'male') & (df.Survived == 1)), ' || ', 'Died Male: ',
#       np.sum((df.Sex == 'male') & (df.Survived == 0)))
# print('Survived Female: ', np.sum((df.Sex == 'female') & (df.Survived == 1)), ' || ', 'Died Female: ',
#       np.sum((df.Sex == 'female') & (df.Survived == 0)))

# Print name(s) of the person whose age is missing.
# print(df['Name'].where(df['Age'].isnull()).unique())

# Print indexes in which fare is missing.
# print(df['PassengerId'].where(df['Fare'] == 0).unique())

# Fill null values of age by mean of age and Mode in Cabin and Embarked
df['Age'] = df['Age'].fillna(int(df['Age'].mean()))

# label_encode = LabelEncoder()
# cabin_label = label_encode.fit_transform(df['Cabin'])
# mode = statistics.mode(cabin_label)
# fill_value = df['Cabin'].where(cabin_label)
# print(fill_value)
# print(df['Cabin'].fillna(fill_value)

# store_fillna = df['Cabin'].mode()[0]
# df['Cabin'].fillna(store_fillna, inplace=True)
# print(df['Cabin'])

# store_fillna = df['Embarked'].mode()[0]
# df['Embarked'].fillna(store_fillna, inplace=True)
# print(df)

#  Print count of travelers whose age is below 12 yrs.
# below_age = df['PassengerId'].where(df['Age'] < 12)
# print(below_age.count())

#  Print youngest person and oldest person traveling in titanic.
# df['young'] = df['Name'].where((df['Age'] > 18) & (35 >= df['Age']))
# df['old'] = df['Name'].where(df['Age'] >= 36)
# print('Young: ', df['young'].count(), ' || ', 'Old: ', df['old'].count())

# Print count of travellers below 12 years who lost their lives.
# df['below_12_died'] = df['Name'].where((df['Age'] < 12) & (df['Survived'] == 0))
# print(df['below_12_died'].count())

#  Print a graph with survived and death ( multiple bar graph ) in age groups
# ( multiple variables / list / data frame allowed )
# Age          Survived              Deaths        Total
# 00-10           ….                       ….               ….
# 10-20           ….                       ….               ….
# 20-30           …..                      ….
# 40-50
# …….
# x_axis = np.arange(5)
# gap = 0.2
# Age = ['Below 10', '11 to 20', '21 to 30', '31 to 40', 'Above 41']
#
# s1 = df['Name'].where((df['Survived'] == 1) & (df['Age'] <= 10))
# s2 = df['Name'].where((df['Survived'] == 1) & (df['Age'] <= 20) & (11 <= df['Age']))
# s3 = df['Name'].where((df['Survived'] == 1) & (21 <= df['Age']) & (df['Age'] <= 30))
# s4 = df['Name'].where((df['Survived'] == 1) & (31 <= df['Age']) & (df['Age'] <= 40))
# s5 = df['Name'].where((df['Survived'] == 1) & (41 <= df['Age']))
#
# Survived1 = np.array([s1.count(), s2.count(), s3.count(), s4.count(), s5.count()])
# Survived = Survived1.tolist()
#
# d1 = df['Name'].where((df['Survived'] == 0) & (df['Age'] <= 10))
# d2 = df['Name'].where((df['Survived'] == 0) & (df['Age'] <= 20) & (11 <= df['Age']))
# d3 = df['Name'].where((df['Survived'] == 0) & (21 <= df['Age']) & (df['Age'] <= 30))
# d4 = df['Name'].where((df['Survived'] == 0) & (31 <= df['Age']) & (df['Age'] <= 40))
# d5 = df['Name'].where((df['Survived'] == 0) & (41 <= df['Age']))
#
# Died1 = np.array([d1.count(), d2.count(), d3.count(), d4.count(), d5.count()])
# Died = Died1.tolist()
#
# Total = Survived1 + Died1
# Total = Total.tolist()
#
# a = plt.bar(x_axis - gap, Survived, gap, label='Survived')
# b = plt.bar(x_axis, Died, gap, label='Died')
# c = plt.bar(x_axis + gap, Total, gap, label='Total')
#
# plt.bar_label(a, Survived)
# plt.bar_label(b, Died)
# plt.bar_label(c, Total)
#
# plt.xticks(x_axis, Age)
# plt.xlabel('Age Group')
# plt.ylabel('Total count')
# plt.legend(title='Data')
# plt.show()

''' Problem 15 : Perform label encoding if required. '''
new_data = pd.read_csv('train.csv')

encoder = LabelEncoder()
new_data['labeled_sex'] = encoder.fit_transform(new_data['Sex'])
new_data['labeled_Embarked'] = encoder.fit_transform(new_data['Embarked'])

''' Problem 16 : Divide data in training and testing data ( train test split ). '''
X = new_data[['labeled_Embarked', 'labeled_sex', 'Age']]
y = new_data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

''' Problem 17 : Perform Random Forest Machine learning on Titanic dataset. '''
model = ensemble.RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

predictor = model.predict(X_test)

print('The Accuracy is : ', model.score(X_test, y_test))
