import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1])) # Destination, Cost
            
        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))
        
        while pq:
            cur_cost, cur_des = heapq.heappop(pq)
            if cur_des not in costs:
                costs[cur_des] = cur_cost
                for next_cost, next_des in graph[cur_des]:
                    next_cost += cur_cost
                    heapq.heappush(pq, (next_cost, next_des))
                    
        for node in range(1, n+1):
            if node not in costs:
                return -1
        
        return max(costs.values())