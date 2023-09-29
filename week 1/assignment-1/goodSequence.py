n = int(input())
a = list(map(int, input().split()))

# a = []

# for i in range(n):
#     a.append(int(input()))

count = 0
freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    if freq[i] < i:
        count += freq[i]
    elif freq[i] > i:
        count += freq[i] - i

print(count)