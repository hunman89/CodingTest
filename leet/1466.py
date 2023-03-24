class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.check = set()
        self.answer = 0
        for i, j in connections:
            if i < j:
                self.graph[i].append([j, True])
                self.graph[j].append([i, True])
            else:
                self.graph[i].append([j, False])
                self.graph[j].append([i, False])
        self.dfs(0)
        return self.answer
        
    def dfs(self, node):        
        self.check.add(node)
        for n_node, flag in self.graph[node]:
            if n_node not in self.check:
                if node < n_node:
                    if flag:
                        self.answer += 1                    
                else:
                    if not flag:
                        self.answer += 1
                self.dfs(n_node)