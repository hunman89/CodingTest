from typing import List
import collections
import heapq

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for m, n, v in flights:
        graph[m].append((n, v))

    Q = [(0, src, K)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for next_node, next_price in graph[node]:
                all_price = price + next_price
                heapq.heappush(Q, (all_price, next_node, k-1))
    
    return -1

print (findCheapestPrice(n,flights,src,dst,k))