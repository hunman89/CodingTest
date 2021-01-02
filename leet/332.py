from typing import List
import collections

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []
    def dfs(city):        
        while graph[city]:
            dfs(graph[city].pop())
        route.append(city)
    
    dfs("JFK")
    return route[::-1]


print (findItinerary(tickets))