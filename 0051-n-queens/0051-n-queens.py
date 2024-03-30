class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 열, 대각선 확인하는 func
        def is_valid(board, row, col):
            #열
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            #오른쪽 대각선
            i, j = row-1, col+1
            while i>=0 and j<n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            
            #왼쪽 대각선
            i, j = row-1, col-1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            
            return True
        
        def solution(row):
            # 줄이 최종에 닿았을때,
            if row == n:
                answer.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    solution(row+1)
                    board[row][col] = '.'
        
        answer = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solution(0)
        
        return answer