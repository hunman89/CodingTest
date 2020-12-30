import collections
jewels = "aA"
stones = "aAAbbbb"

print(sum(s in jewels for s in stones))
'''
count = 0
hash = collections.Counter(stones)
print(hash)

for char in jewels:
  count += hash[char]

print(count)
'''

'''
hash = {}
for char in stones:
  if char not in hash:
    hash[char] = 1
  else:
    hash[char] += 1

print(hash)

count = 0
for char in jewels:
  if char in hash:
    count += hash[char]

print(count)
'''