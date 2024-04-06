import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
import warnings

warnings.filterwarnings('ignore', 'X does not have valid feature names')

df = pd.read_csv('brazil-stadium.csv')
# print(df.isnull())
# print(df.isnull().sum())

# Converting in categories
df['Stadium_Name'] = df['Stadium_Name'].astype('category')
df['Locality'] = df['Locality'].astype('category')
df['Federative_Units'] = df['Federative_Units'].astype('category')
df['Owner'] = df['Owner'].astype('category')
# print(df)

# assigning numerical label
df['Stadium_Name'] = df['Stadium_Name'].cat.codes
df['Locality'] = df['Locality'].cat.codes
df['Federative_Units'] = df['Federative_Units'].cat.codes
df['Owner'] = df['Owner'].cat.codes
# print(df)

enc = OneHotEncoder()
encoded_df = pd.DataFrame(enc.fit_transform(df[['Stadium_Name', 'Locality', 'Federative_Units', 'Owner']]).toarray())
print(encoded_df)

newdf = df.join(encoded_df)
# print(newdf)

reg = LinearRegression()
reg.fit(df[['Stadium_Name', 'Locality', 'Federative_Units', 'Owner']], df[['Capacity']])
# print(np.floor(reg.predict([[1, 1, 2, 1]])))
