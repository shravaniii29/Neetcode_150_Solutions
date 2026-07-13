# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in numSet:

            # Check if num is the start of a sequence
            if num - 1 not in numSet:

                current = num
                length = 1

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest