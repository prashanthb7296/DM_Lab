# Program 1: Knowledge Discovery in Databases (KDD)

import numpy as np
import pandas as pd

# Original data
data = {
    "Name": ["Anil", "Bharath", "Charan", "Deepa", "Farah"],
    "Age": [24, 26, 25, 28, 27],
    "Salary": [35000, 42000, np.nan, 50000, 48000]
}

df = pd.DataFrame(data)

# 1. Data selection
selected = df[["Name", "Age", "Salary"]].copy()

# 2. Data preprocessing
median_salary = selected["Salary"].median()
selected["Salary"] = selected["Salary"].fillna(median_salary)

# 3. Data transformation
selected["Salary_in_Thousands"] = (
    selected["Salary"] / 1000
).astype(int)

selected["Age_Group"] = pd.cut(
    selected["Age"],
    bins=[0, 25, 30],
    labels=["Up to 25", "26 to 30"],
    include_lowest=True
)

print("Median salary used:", median_salary)
print("Final transformed dataset:")
print(selected.to_string(index=False))