import collections
import heapq

#route = [[5,1,15], [4,2,6], [1,4,8], [3,2,10], [1,2,7], [5,4,6], [2,5,11]]
route = [[1,2,1], [1,3,4], [2,3,2]]

def solution(route):
    result = []
    graph = collections.defaultdict(list)
    for u, v, w in route:
        graph[u].append((v, w))
    Q = [(0, 1)]
    dist = collections.defaultdict(int) 
    while Q:
        gas, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = gas
            for v, w in graph[node]:
                alt = max(gas, w)
                heapq.heappush(Q, (alt, v))
    return dist

print(solution(route))