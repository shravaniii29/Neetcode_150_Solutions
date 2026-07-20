# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

#OPTIMAL SOLUTION:
# Approach: Two Pointers
# Keep two pointers at both ends and maintain the maximum height seen
# from the left and right. The smaller maximum height determines the
# water trapped at that side, so move that pointer inward and update
# the trapped water.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        water = 0

        while left < right:

            if leftMax < rightMax:

                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]

            else:

                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]

        return water
    
    
#BRUTE FORCE APPROACH:
# Approach: Brute Force
# For every bar, find the tallest bar on its left and right.
# The water trapped above the current bar is:
# min(leftMax, rightMax) - current height.
# Add the trapped water for every bar.

# Time Complexity: O(n²)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0
        n = len(height)

        for i in range(n):

            leftMax = 0
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])

            rightMax = 0
            for j in range(i, n):
                rightMax = max(rightMax, height[j])

            total_water += min(leftMax, rightMax) - height[i]

        return total_water    