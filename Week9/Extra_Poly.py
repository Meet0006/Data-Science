import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt

poly_data = pd.read_csv('Position_Salaries.csv')

poly_x = PolynomialFeatures(degree=6).fit_transform(poly_data[['Level']])

reg = linear_model.LinearRegression()
reg.fit(poly_x, poly_data[['Salary']])

plt.scatter(poly_data.Level, poly_data.Salary)
plt.plot(poly_data.Level, reg.predict(poly_x))
plt.show()
