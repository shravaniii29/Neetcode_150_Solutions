#Two Pointer Ques
# Question - Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2],
# such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.
# Your solution must use O(1) additional space.


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            current = numbers[left] + numbers[right]

            if current == target:
                return [left+1, right+1]

            elif current < target:
                left += 1

            else:
                right -= 1
        

# Approach: Two Pointers
# Since the array is sorted, use left and right pointers.
# If the sum is less than target, move left forward to increase the sum.
# If the sum is greater than target, move right backward to decrease the sum.
# Return the 1-indexed positions when the target sum is found.
#
# Time Complexity: O(n) - each pointer moves at most n times.
# Space Complexity: O(1) - only two pointers and a sum variable are used.