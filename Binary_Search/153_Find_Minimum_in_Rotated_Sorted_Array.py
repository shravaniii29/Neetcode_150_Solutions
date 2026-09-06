class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is on the left side (including mid)
            else:
                right = mid

        return nums[left]

# TC: O(log n)
# SC: O(1)