class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.score = math.inf
        self.visited = [0 for i in range(n + 1)]
        self.graph = defaultdict(dict)
        self.distances = {}
        for i, j, v in roads:
            self.graph[i][j] =  self.graph[j][i] = v
        
        self.dfs(1)
        return self.score
        
    def dfs(self, node):
        if self.visited[node] == 1: return
        self.visited[node] = 1
        for next_node, v in self.graph[node].items():
            self.score = min(self.score, v)
            self.dfs(next_node)
