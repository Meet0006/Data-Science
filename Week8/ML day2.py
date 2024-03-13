from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model
import warnings

warnings.filterwarnings("ignore", message="X does not have valid feature names")
insurance = pd.read_csv('insurance.csv')

# Find output through single input

reg = linear_model.LinearRegression()
reg.fit(insurance[['age']], insurance['charges'])

print(reg.intercept_, reg.coef_)
print(reg.predict([[19]]))

plt.scatter(insurance['age'], insurance['charges'], color='pink')
plt.plot(insurance['age'], reg.predict(insurance[['age']]))
plt.show()

# Find output through multiple input

reg = linear_model.LinearRegression()
reg.fit(insurance[['age', 'bmi', 'children']], insurance['charges'])

print(reg.intercept_, reg.coef_)
print(reg.predict([[19, 89, 4]]))

plt.scatter(insurance['age'], insurance['charges'], color='red')
plt.scatter(insurance['bmi'], insurance['charges'], color='green')
plt.scatter(insurance['children'], insurance['charges'], color='black')
plt.show()

# Multi value linear regression

order = pd.read_csv('orderdata.csv')

reg = linear_model.LinearRegression()
reg.fit(order[['users', 'orders', 'age']], order['amount'])

print(reg.intercept_, reg.coef_)
print(reg.predict([[19, 89, 4]]))

plt.scatter(order['users'], order['amount'], color='red')
plt.scatter(order['orders'], order['amount'], color='green')
plt.scatter(order['age'], order['amount'], color='black')
plt.plot(order['users'], reg.predict(order[['users', 'orders', 'age']]))
plt.plot(order['orders'], reg.predict(order[['users', 'orders', 'age']]))
plt.plot(order['age'], reg.predict(order[['users', 'orders', 'age']]))
plt.show()
