# Calculate Support Value of an Itemset

transactions = [
    ["Milk", "Bread"],
    ["Milk", "Eggs"],
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk", "Bread"]
]

itemset = {"Milk", "Bread"}
transaction_sets = [set(t) for t in transactions]

support_count = sum(
    itemset.issubset(transaction)
    for transaction in transaction_sets
)

support = support_count / len(transaction_sets)

print("Itemset:", sorted(itemset))
print("Support count:", support_count)
print(f"Support value: {support:.2f}")