import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

plr = pd.read_csv('orders.csv')

poly_x = PolynomialFeatures().fit_transform(plr[['slot']])

reg = linear_model.LinearRegression()
reg.fit(poly_x, plr[['amount']])

print(reg.predict(PolynomialFeatures().fit_transform([[8]])))

plt.scatter(plr.slot, plr.amount)
plt.plot(plr.slot, reg.predict(poly_x))
plt.show()
