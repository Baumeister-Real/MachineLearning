from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('FuelConsumptionCo2.csv')
data.head()
data = data[["ENGINESIZE", "CO2EMISSIONS"]]

train = data[:int(len(data)*.8)]
test = data[int(len(data)*.8):]

regr = linear_model.LinearRegression()

train_x = np.array(train[["ENGINESIZE"]])
train_y = np.array(train[["CO2EMISSIONS"]])

regr.fit(train_x, train_y)

plt.scatter(data["ENGINESIZE"], data["CO2EMISSIONS"], color="blue")
plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')
plt.xlabel("ENGINESIZE")
plt.ylabel("CO2EMISSIONS")
#plt.show()

def get_regress_pred(input_features, intercept, slope):
    predicted_values = input_features*slope + intercept
    return predicted_values

example_engine_size = 3.5
estimated_emissions = get_regress_pred(example_engine_size, regr.intercept_[0],
                                       regr.coef_[0][0])
print("Estimated emission in " + str(estimated_emissions))

test_x = np.array(test[["ENGINESIZE"]])
test_y = np.array(test[["CO2EMISSIONS"]])
test_y_ = regr.predict(test_x)

print("Mean absolute error %.2f" %np.mean(np.absolute(test_y_ - test_y)))
print("Mean sum of squares (MSE): %.2f" %np.mean((test_y_-test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_, test_y))