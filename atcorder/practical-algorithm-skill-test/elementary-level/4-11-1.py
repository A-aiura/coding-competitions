from collections import Counter

# input
S = list(input())

# counter dictionary
c = Counter(S)

# sort to most common alphabet order
ans = c.most_common()[0]

# print answer
print(ans[0])
