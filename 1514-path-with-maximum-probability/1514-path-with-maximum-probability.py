from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):

        graph = defaultdict(list)
        
        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
            
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]
        
        while pq:
            cur_prob, cur_v = heapq.heappop(pq)
            
            for next_v, path_prob in graph[cur_v]:
                if -cur_prob * path_prob > max_prob[next_v]:
                    max_prob[next_v] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[next_v], next_v))

        
        return max_prob[end]
                    
#         graph = defaultdict(list)
#         for i, (u, v) in enumerate(edges):
#             graph[u].append((v, succProb[i]))
#             graph[v].append((u, succProb[i]))
#         max_prob = [0.0] * n
#         max_prob[start] = 1.0
#         pq = [(-1.0, start)] # 최대값으로 하기 위해

#         while pq:
#             cur_prob, cur_v = heapq.heappop(pq)

#             for next_v, path_prob in graph[cur_v]:
#                 if -cur_prob * path_prob > max_prob[next_v]:
#                     max_prob[next_v] = -cur_prob * path_prob
#                     heapq.heappush(pq, (-max_prob[next_v], next_v))
                    
#         return max_prob[end]