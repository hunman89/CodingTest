class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # graph 생성
        connect = defaultdict(set)
        for i,j in edges:
            connect[i].add(j)
            connect[j].add(i)
        
        # graph 순회 하면서 apple까지 가는 경로 모두 hasApple True
        def dfs(node, prev):
            for next_node in connect[node]:
                if next_node != prev and dfs(next_node, node):
                    hasApple[node] = True
            return hasApple[node]
        dfs(0,-1)

        # 거리 계산
        if sum(hasApple) == 0: return 0
        return(sum(hasApple)-1) *2