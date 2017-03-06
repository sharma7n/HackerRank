from collections import Counter


a, b = (input().strip().lower() for _ in range(2))
a_occurs, b_occurs = Counter(a), Counter(b)
common_letters = set(a_occurs.keys()) | set(b_occurs.keys())
min_deletions = sum(abs(a_occurs[letter] - b_occurs[letter])
    for letter in common_letters)
print(min_deletions)