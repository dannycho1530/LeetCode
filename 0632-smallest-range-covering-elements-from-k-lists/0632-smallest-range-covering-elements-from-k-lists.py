import sys
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        n = len(nums)
        
        max_num = -sys.maxsize
        
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_num = max(max_num, nums[i][0])
        
        answer = [pq[0][0], max_num]
        index_list = [0] * len(nums)
        
        while True:
            _, i, j = heapq.heappop(pq)
            index_list[i] += 1
            # 종료 시점
            if j == len(nums[i])-1:
                break
            
            next_num = nums[i][index_list[i]]

            heapq.heappush(pq, (next_num, i, j+1))
            max_num = max(next_num, max_num)
            
            if answer[1] - answer[0] > max_num - pq[0][0]:
                answer = [pq[0][0], max_num]
    
        return answer