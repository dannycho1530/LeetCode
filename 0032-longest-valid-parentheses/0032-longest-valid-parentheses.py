class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        temp = [-1]        
        for i, j in enumerate(s):
            if j == '(':
                temp.append(i)
                
            else:
                temp.pop()
                if not temp:
                    temp.append(i)
                else:
                    answer = max(answer, i - temp[-1])

        return answer
            
            