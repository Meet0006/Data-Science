from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

# Read csv file
lr = pd.read_csv('LR.csv')

# Add values
X = np.array(lr['X'])
Y = np.array(lr['Y'])

# Method 1
# Calculus
slop, inter = np.polyfit(X, Y, 1)
regre_line = inter + slop * X
#
# # Create scatter
plt.scatter(X, Y, label='Data')
plt.plot(X, regre_line, label='Regression Line')
plt.grid(True)
plt.xlabel('Area')
plt.ylabel('Price')
plt.legend()
plt.show()

# Method 2
meanx = np.mean(X)
meany = np.mean(Y)
above_eq = np.sum((meanx - X) * (meany - Y))
below_eq = np.sum((meanx - X) ** 2)
b1 = above_eq / below_eq
b0 = meany - (b1 * meanx)
lin_re = b0 + (b1 * X)

plt.scatter(X, Y)
plt.plot(X, lin_re)

plt.show()

# Method3
Price = pd.read_csv("prices.csv")
plt.scatter(Price.area, Price.price, color='green')

reg = linear_model.LinearRegression()
reg.fit(Price[['area']], Price[['price']])
print(reg.predict(np.array([3300]).reshape(-1, 1)))

print(reg.intercept_)  # B0
print(reg.coef_)  # B1

plt.plot(Price.area, reg.predict(Price[['area']]))
plt.show()
