# height -> 빗물이 저장될 블록의 높이 정보가 저장된 리스트
# trapping rain water -> 한칸에 물이 가두어지려면 해당 칸의 좌측, 우측에 높이가 해당칸의 높이보다 더 큰 칸이 존재해야한다.
    # 이후로 해당 칸보다 더 높이가 큰 좌측, 우측 칸을 벽이라고 부른다.
    # 가두어지는 물의 양은 우측 벽 중 높이가 더 작은칸의 높이와 해당 칸의 높이의 차이이다.
    # 앞에서부터 탐색 or 투포인터
    


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
		# 맨 왼쪽, 오른쪽 칸을 벽으로 설정한다.
        left_max, right_max = height[left], height[right]
		# 모든 칸을 확인할 때 까지 반복한다.
        while left < right:
			# 우측 벽의 높이가 좌측 벽의 높이보다 큰 경우
            if left_max <= right_max:
				# 좌측 벽의 옆을 확인한다.
                left += 1
				# 내부 칸의 높이가 좌측 벽보다 작은 경우 물을 채운다.
                if height[left] < left_max:
                    answer += left_max - height[left]
					# 내부 칸의 높이가 좌측 벽보다 큰 경우 해당 칸을 새로운 좌측 벽으로 설정한다.
                else:
                    left_max = height[left]
					# 좌측 벽의 높이가 우측 벽의 높이보다 큰 경우
            else:
				# 우측 벽의 옆을 확인한다.
                right -= 1
				# 내부 칸의 높이가 우측 벽보다 작은 경우 물을 채운다.
                if height[right] < right_max:
                    answer += right_max - height[right]
				# 내부 칸의 높이가 우측 벽보다 큰 경우 해당 칸을 새로운 우측 벽으로 설정한다.
                else:
                    right_max = height[right]
        return answer