from collections import Counter


m, n = (int(e) for e in input().split(' '))
magazine = Counter(input().strip().split(' '))
note = Counter(input().strip().split(' '))

if all(note[word] <= magazine[word] for word in note):
    print("Yes")
else:
    print("No")