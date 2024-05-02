class Solution:

    def numIslands(self, grid):
        answer = 0
        direction = [(0,1), (0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            visited[r][c] = True
            
            for a, b in direction:
                next_r = r + a
                next_c = c + b
                if isValid(next_r, next_c, rows, cols):
                    if grid[next_r][next_c] == '1' and not visited[next_r][next_c]:
                        dfs(next_r, next_c)
           
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    answer += 1
                    
        return answer
                
                
                
def isValid(r, c, row_len, col_len):
    return (r>=0 and r<row_len) and (c>=0 and c<col_len)
  