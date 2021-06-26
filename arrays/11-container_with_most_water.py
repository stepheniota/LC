'''
leetcode 11 - Container with Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if height[left + 1] >= height[right - 1]:
                    left += 1
                else:
                    right -= 1

        return max_area
