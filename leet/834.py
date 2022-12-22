class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        
        def dfs(node, parent):
            subtree_size[node] = 1
            for child in tree[node]:
                if child == parent:
                    continue
                dfs(child, node)
                subtree_size[node] += subtree_size[child] # 하위 트리의 사이즈 측정, 자기자신 = 1
                sum_of_distances[node] += sum_of_distances[child] + subtree_size[child] # 하위 트리들의 거리 측정, 자기 자신 = 0
        
        def dfs2(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                sum_of_distances[child] = sum_of_distances[node] - subtree_size[child] + (n - subtree_size[child])
                dfs2(child, node)
        
        subtree_size = [0] * n
        sum_of_distances = [0] * n
        dfs(0, None)
        print(subtree_size, sum_of_distances)
        dfs2(0, None)
        return sum_of_distances
        
        # if n ==1:
        #     return [0]
        # answer = [0] * n
        # tree = collections.defaultdict(set)
        # for i, j in edges:
        #     tree[i].add(j)
        #     tree[j].add(i)
        # legs = {k:len(v) for k, v in tree.items()}
        
        # def dfs(now, before, depth):
        #     d[now] = depth
        #     for i in tree[now]:
        #         if i != before:
        #             dfs(i, now, depth+1)

        # for i in range(n):
        #     d = [0] * n
        #     dfs(i,-1,1)
        #     print(d)
        #     sum_i = 0
        #     for j in range(n):
        #         if j == i:
        #             sum_i += legs[j] * d[j]
        #         else:
        #             sum_i += (legs[j] - 1) *d[j]
        #     answer[i] = sum_i

        # return answer

        #-------

        # if n == 1:
        #     return [0]

        # answer = [0] * n
        # graph = defaultdict(list)
        # for i, j in edges:
        #     graph[i].append(j)
        #     graph[j].append(i)

        # def dfs(e, step, depth):
        #     step[e] = 1
        #     next_nodes = 0
        #     sums = 0
        #     for next_e in graph[e]:
        #         if step[next_e] == 0:
        #             next_nodes += 1
        #             sums += (depth) + dfs(next_e, step, depth + 1)
        #     if next_nodes == 0: 
        #         return 0
        #     else:
        #         return sums

        # for i in range(n):
        #     step = [0] * n
        #     answer[i] = dfs(i, step, 1)
        
        # return answer