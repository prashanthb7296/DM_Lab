# Program 4: Classify Loan Applications Using the Decision Tree Algorithm

import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import (
    DecisionTreeClassifier, export_text, plot_tree
)

income = [25000, 30000, 35000, 50000, 60000, 70000]
age = [22, 25, 30, 35, 40, 45]

loan_status = [
    "Reject", "Reject", "Reject",
    "Approve", "Approve", "Approve"
]

x = np.column_stack((income, age))
y = np.array(loan_status)

model = DecisionTreeClassifier(random_state=42, max_depth=3)
model.fit(x, y)

prediction = model.predict([[45000, 32]])[0]

print("Prediction for [45000, 32]:", prediction)
print(f"Training accuracy: {model.score(x, y) * 100:.2f}%")
print(export_text(model, feature_names=["Income", "Age"]))

plt.figure(figsize=(9, 4))
plot_tree(
    model,
    feature_names=["Income", "Age"],
    class_names=model.classes_,
    filled=True,
    rounded=True
)

plt.title("Decision Tree for Loan Classification")
plt.tight_layout()
plt.show()