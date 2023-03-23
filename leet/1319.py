class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        self.parent = [i for i in range(n)]
        for i, j in connections:
            self.union(i,j)
        
        # 최종적으로 합쳐준다.
        for k in range(n):
            if self.parent[k] != k:
                self.parent[k] = self.find_parent(k)
        return len(set(self.parent)) - 1

    #union find
    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        a = self.find_parent(a)
        b = self.find_parent(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b