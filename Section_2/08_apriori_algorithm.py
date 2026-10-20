# Program 8: Apriori Algorithm

from itertools import combinations
from math import ceil

transactions = [
    {"Milk", "Bread", "Eggs"},
    {"Milk", "Bread"},
    {"Milk", "Eggs"},
    {"Bread", "Butter"},
    {"Milk", "Bread", "Butter"}
]

minimum_support = 0.40
minimum_count = ceil(minimum_support * len(transactions))

def support_count(itemset):
    return sum(itemset.issubset(t) for t in transactions)

# Generate frequent 1-itemsets
items = sorted({item for t in transactions for item in t})
candidates = {frozenset([item]) for item in items}

current_level = {
    itemset: support_count(itemset)
    for itemset in candidates
    if support_count(itemset) >= minimum_count
}

all_frequent = []
k = 1

while current_level:
    all_frequent.extend(current_level.items())
    previous = set(current_level)
    k += 1

    # Join step
    candidates = {
        left | right
        for left in previous
        for right in previous
        if len(left | right) == k
    }

    # Prune candidates having an infrequent subset
    candidates = {
        candidate for candidate in candidates
        if all(
            frozenset(subset) in previous
            for subset in combinations(candidate, k - 1)
        )
    }

    current_level = {
        itemset: support_count(itemset)
        for itemset in candidates
        if support_count(itemset) >= minimum_count
    }

all_frequent.sort(
    key=lambda entry: (len(entry[0]), sorted(entry[0]))
)

for itemset, count in all_frequent:
    support = count / len(transactions)
    name = ", ".join(sorted(itemset))
    print(f"{{{name}}}: count={count}, support={support:.2f}")