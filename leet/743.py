from typing import List
import collections
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for i,j,k in times:
        graph[i].append((j,k))

    # 큐 변수(소요시간, 정점node)
    Q = [(0, K)]
    # 정점에 대한 소요시간을 나타낸 자료구조, 방문여부 확인
    dist = collections.defaultdict(int)

    while Q:
        # Q에서 소요시간이 최소인 정점을 빼낸다.
        time, node = heapq.heappop(Q)
        # 그 점이 dict에 없으면
        if node not in dist:
            # 삽입
            dist[node] = time
            # 그래프에서 그 점에서 도달할 수 있는 정점과 시간을 찾아
            for next_node, next_time in graph[node]: 
                # 기존 시간과 합해 총 시간을 구하고
                all_time = time + next_time
                # 큐 변수에 넣는다/ (소요시간, 정점)의 형식으로
                heapq.heappush(Q, (all_time, next_node))
    
    # 모든 점에 방문했다고 하면,
    if len(dist) == N:
        # 최대값 = 총 통신 소요시간
        return max(dist.values())
    return -1

print (networkDelayTime(times,N,K))