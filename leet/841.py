class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        # visits = set()

        # def dfs(room):
        #     if room not in visits:
        #         visits.add(room)
        #         for n_room in rooms[room]:
        #             dfs(n_room)
        # dfs(0)
        # return len(visits) == n

        visits = [0] * n
        
        def dfs(room):
            if visits[room] is 0:
                visits[room] = 1
                for n_room in rooms[room]:
                    dfs(n_room)
        dfs(0)
        return sum(visits) == n