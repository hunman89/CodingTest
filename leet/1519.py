class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # graph = defaultdict(set)
        # answer = [0] * n
        # sub_labels = [""] * n
        # cache = {}
        # for i,j in edges:
        #     graph[i].add(j)
        #     graph[j].add(i)
        
        # def dfs(node, prev):
        #     sub_labels[node] = labels[node]
        #     for i in graph[node]:
        #         if i != prev:
        #             dfs(i, node)
        #             sub_labels[node] += sub_labels[i]
        #     answer[node] = sub_labels[node].count(labels[node])

        # dfs(0,-1)

        # return answer

        graph = defaultdict(set)
        answer = [0] * n
        cache = {}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        def dfs(node, prev):
            cache_item = {}
            cache_item[labels[node]] = 1
            cache[node] = cache_item
            for i in graph[node]:
                if i != prev:
                    dfs(i, node)
                    dict_com = defaultdict(int)
                    for d in (cache[node], cache[i]):
                        for k, v in d.items():
                            dict_com[k] += v
                    cache[node] = dict_com
            answer[node] = cache[node][labels[node]]
        dfs(0,-1)

        return answer