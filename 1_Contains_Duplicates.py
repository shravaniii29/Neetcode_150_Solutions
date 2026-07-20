#ARRAY PROBLEM - EASY
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # very important to sort the array first, so that duplicates are adjacent to each other
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                return True
            i += 1
            nums[i] = nums[j]

        return False