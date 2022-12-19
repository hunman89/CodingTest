class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # if n is 1:
        #     return True
        
        node = defaultdict(list)
        for v1, v2 in edges:
            node[v1].append(v2)
            node[v2].append(v1)

        def step(v, check):
            if v == destination:
                return True
            if v in check:
                return False
            check.add(v)
            for n_v in node[v]:
                if step(n_v, check):
                    return True
            return False

        check = set()
        return step(source, check)

        # node = {}
        # for vertex1, vertex2 in edges:
        #     if vertex1 not in node.keys():
        #         node[vertex1] = set([vertex2])
        #     else:
        #         node[vertex1].add(vertex2)

        #     if vertex2 not in node.keys():
        #         node[vertex2] = set([vertex1])
        #     else:
        #         node[vertex2].add(vertex1)
        
        # self.check = [0] * n
        # def step(self, vertex):
        #     self.check[vertex] += 1
        #     for n_step in node[vertex]:
        #         if self.check[n_step] is 0:
        #             step(self, n_step)
        # step(self, source)       
        # return self.check[destination] > 0