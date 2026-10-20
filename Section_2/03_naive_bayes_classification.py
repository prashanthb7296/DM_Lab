# Program 3: Classify Students Using Gaussian Naive Bayes

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

hours = np.array([[2], [3], [4], [5], [6], [7]])
result = np.array(["Fail", "Fail", "Pass", "Pass", "Pass", "Pass"])

x_train, x_test = hours[:4], hours[4:]
y_train, y_test = result[:4], result[4:]

model = GaussianNB().fit(x_train, y_train)

predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
new_prediction = model.predict([[4.5]])[0]

print("Actual test results  :", y_test.tolist())
print("Predicted test results:", predictions.tolist())
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Prediction for 4.5 study hours:", new_prediction)