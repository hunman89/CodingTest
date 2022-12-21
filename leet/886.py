class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        uf = UnionFind(n)
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, n+1):
            parent_i = uf.find(i) # i의 부모노드를 찾는다.
            if parent_i in self.graph:
                parent_dislike_i = uf.find(self.graph[i][0])  # i가 싫어하는 노드중 하나의 부모노드를 찾는다.
                for dis in self.graph[i][1:]:                 # 나머지 i가 싫어하는 노드들을 순회하면서
                    if not uf.union(dis, parent_dislike_i, parent_i): return False   # 그룹화 한다. 이때 i의 부모 노드와 겹치지 않는지 확인하고, 겹치면 False를 리턴하게.
        return True      

class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n+1)]
    
    def find(self, i): # 재귀를 통해 i의 부모노드를 찾아간다.
        if i != self.p[i]: # 부모 노드가 자기 자신이 아닐때 
            self.p[i] = self.find(self.p[i]) # 재귀를 통해 부모를 찾고 그 값을 저장한다.
        return self.p[i]

    def union(self, j, parent_dislike_i, parent_i): # j를 parent_dislike_i와 그룹화 한다.
        parent_j = self.find(j) # j의 부모를 찾고
        self.p[parent_j] = parent_dislike_i # j의 부모노드의 부모를 parent_dislike_i로 만들어 그룹화 한다.
        return parent_j != parent_i # j의 부모가 i의 부모와 겹치지 않는지(그룹이 분리되는지 확인)