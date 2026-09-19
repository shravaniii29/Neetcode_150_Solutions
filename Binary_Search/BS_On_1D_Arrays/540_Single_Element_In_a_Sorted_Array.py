#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

#Return the single element that appears only once.

#Your solution must run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even so we can compare it with the next element.
            if mid % 2 == 1:
                mid -= 1

            # If the pair is correct, the single element is on the right.
            if nums[mid] == nums[mid + 1]:
                left = mid + 2

            # Otherwise, the single element is at mid or on the left.
            else:
                right = mid

        # left == right, so this is the single element.
        return nums[left]


# Time Complexity: O(log n)
# Space Complexity: O(1)


#Brute Force Approach: (comparing each element with its next and previous element)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return arr[0]

        for i in range(n):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            elif i == n - 1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if (nums[i] != nums[i+1] and nums[i]!=nums[i-1]):
                    return nums[i]