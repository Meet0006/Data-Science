import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn import tree
import warnings

warnings.filterwarnings('ignore', message='X does not have valid feature names')

# Q1
tenis = pd.read_csv('PlayTennis.csv')

label_encode = preprocessing.LabelEncoder()
# label_encode = preprocessing.OneHotEncoder()

outlook_e = label_encode.fit_transform(tenis['Outlook'])
temp_e = label_encode.fit_transform(tenis['Temperature'])
humidity_e = label_encode.fit_transform(tenis['Humidity'])
wind_e = label_encode.fit_transform(tenis['Wind'])

# Q2
car = pd.read_csv('cars.csv')

label_encode = preprocessing.LabelEncoder()

brand_e = label_encode.fit_transform(car['brand'])
fuel_e = label_encode.fit_transform(car['fuel'])
owner_e = label_encode.fit_transform(car['owner'])

car['brand'] = brand_e
car['fuel'] = fuel_e
car['owner'] = owner_e

reg = linear_model.LinearRegression()
reg.fit(car[['brand', 'km_driven', 'fuel', 'owner']], car[['selling_price']])
print(reg.predict([[0, 90000, 1, 1]]))

# Q3
tenis = pd.read_csv('PlayTennis.csv')

label_encode = preprocessing.LabelEncoder()

outlook_label = label_encode.fit_transform(tenis['Outlook'])
Temperature_label = label_encode.fit_transform(tenis['Temperature'])
Humidity_label = label_encode.fit_transform(tenis['Humidity'])
Wind_label = label_encode.fit_transform(tenis['Wind'])
PlayTennis = label_encode.fit_transform(tenis['PlayTennis'])

tenis['Outlook'] = outlook_label
tenis['Temperature'] = Temperature_label
tenis['Humidity'] = Humidity_label
tenis['Wind'] = Wind_label
tenis['PlayTennis'] = PlayTennis

reg = tree.DecisionTreeClassifier()
reg.fit(tenis[['Outlook', 'Temperature', 'Humidity', 'Wind']], tenis[['PlayTennis']])
print(np.round(reg.predict([[1, 0, 2, 1]])))
