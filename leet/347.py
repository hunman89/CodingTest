import collections
import heapq

nums = [1,1,1,2,2,3]
k = 2

hash = collections.Counter(nums)
hash_heap = []
for f in hash:
  heapq.heappush(hash_heap, (-hash[f], f))

topk = list()
for _ in range(k):
  topk.append(heapq.heappop(hash_heap)[1])

print(topk)