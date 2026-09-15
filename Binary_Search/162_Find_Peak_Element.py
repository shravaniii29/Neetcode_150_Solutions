#A peak element is an element that is strictly greater than its neighbors.

#Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

#You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If the next element is greater, we are on an increasing slope.
            # So a peak must exist on the right side.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Otherwise, we are on a decreasing slope.
            # So a peak is at mid or somewhere on the left.
            else:
                right = mid

        # left == right, so this index is a peak element.
        return left


# Time Complexity: O(log n)
# Space Complexity: O(1)

