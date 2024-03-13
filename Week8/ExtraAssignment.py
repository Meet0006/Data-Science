from sklearn import linear_model
import pandas as pd
from word2number import w2n
import warnings

warnings.filterwarnings('ignore', 'X does not have valid feature names')

hiring = pd.read_csv('hiring.csv')

median_value = hiring['test_score(out of 10)'].median()
hiring['test_score(out of 10)'] = hiring['test_score(out of 10)'].fillna(median_value)

hiring.experience = hiring['experience'].fillna('0')

store = []
for i in hiring.experience:
    store.append(w2n.word_to_num(i))

hiring.experience = store

reg = linear_model.LinearRegression()
reg.fit(hiring[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], hiring[['salary($)']])

print(reg.intercept_)
print(reg.coef_)

print(17737.26346434 + 2812.95487627 * 12 + 1845.70596798 * 10 + 2205.24017467 * 10)
print(reg.predict([[12, 10, 10]]))
