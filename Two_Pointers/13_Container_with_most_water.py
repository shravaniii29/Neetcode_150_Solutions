#Two Pointer Question
#You are given an integer array heights where heights[i] represents the height of the 
#ith bar.

#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:

            height = min(heights[left], heights[right])
            width = right - left

            water = height * width

            max_water = max(max_water, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Approach: Two Pointers
# Start with pointers at both ends to get the maximum possible width.
# Calculate water using the shorter bar as height and distance as width.
# Move the pointer at the shorter bar, as it limits the container height.
# Keep updating the maximum water area found.

# Time Complexity: O(n) - each pointer moves at most n times.
# Space Complexity: O(1) - only pointer and variable storage is used.