# Program 2: Predict House Prices Using Simple Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

house_size = np.array([1200, 1500, 1800, 2100, 2400])
price = np.array([48, 60, 72, 84, 96])

x = house_size.reshape(-1, 1)
y = price

model = LinearRegression()
model.fit(x, y)

required_size = np.array([[2000]])
predicted_price = model.predict(required_size)[0]

print(f"Slope = {model.coef_[0]:.2f}")
print(f"Intercept = {model.intercept_:.2f}")
print(f"Predicted price for 2000 sq.ft. = Rs. {predicted_price:.2f} lakh")