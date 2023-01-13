class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(set)
        answer = 1 #노드가 1개일 경우 1
        
        for i,v in enumerate(parent):
            if v == -1: continue
            graph[v].add(i)
        
        def dfs(node):
            nonlocal answer
            # 하위 노드 중 최대 길이 2개 저장!
            max1 = max2 = 0
            for i in graph[node]:
                length = dfs(i) # 하위 노드들의 최대 경로 길이 받아옴
                if s[i] != s[node]: # 그 중 s가 다른 하위 노드 중 
                    # 최대 길이 2개 업데이트 max1 > max2
                    if length > max1: 
                        max2 = max1
                        max1 = length
                    elif length > max2:
                        max2 = length
            # max1 + max2 + 1:  s가 다른 하위 노드 중 최대 경로 길이 2개에다 1을 더해 길이 계산
            answer = max(answer, max1 + max2 + 1) # answer에다 최대값 저장
            return max1 + 1 #자신까지 포함해서(길이 계산 뒤 리턴)

        dfs(0)
        return answer