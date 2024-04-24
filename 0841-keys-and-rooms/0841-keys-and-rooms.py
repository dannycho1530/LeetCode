class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0 for _ in range(n)]
        
        
        def dfs(v):
            visited[v] = True
            for next_v in rooms[v]:
                if not visited[next_v]:
                    dfs(next_v)
            
        dfs(0)
        return sum(visited) == n