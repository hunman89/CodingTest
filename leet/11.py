from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left],height[right])*(right - left))
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
    return max_area
 

height = [2,3,10,5,7,8,9]
print(maxArea(height))