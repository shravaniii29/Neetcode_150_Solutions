# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue #Skip the rest of the current iteration and go to the next for loop iteration.

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum < 0:
                    j += 1

                elif current_sum > 0:
                    k -= 1

                else: #condn : current_sum == 0
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result

# Approach: Sorting + Two Pointers
# Sort the array, then fix one element i and use two pointers j and k
# to find two other numbers such that the total sum is 0.
# Move j right if the sum is too small and k left if the sum is too large.
# Skip duplicate values to avoid duplicate triplets.
#
# Time Complexity: O(n^2) - for each i, two pointers scan the remaining array.
# Space Complexity: O(1) - no extra space used apart from the result list.