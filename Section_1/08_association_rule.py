# Program 8: Calculate Confidence of an Association Rule

transactions = [
    ["Milk", "Bread"],
    ["Milk", "Bread", "Butter"],
    ["Milk"],
    ["Bread"],
    ["Milk", "Bread"]
]

transaction_sets = [set(t) for t in transactions]

milk_count = sum("Milk" in t for t in transaction_sets)

milk_bread_count = sum(
    {"Milk", "Bread"}.issubset(t) for t in transaction_sets
)

confidence = milk_bread_count / milk_count

print("Transactions containing Milk:", milk_count)
print("Transactions containing Milk and Bread:", milk_bread_count)
print(f"Confidence of Milk -> Bread: {confidence:.2f}")