#Given an array of integers 'nums' and an integer 'target', return the indices i and j such that nums[i] + nums[j] == target and i != j.

#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_numbers = {} # num : index

        for i in range(len(nums)):
            needed_number = target - nums[i]

            if needed_number in visited_numbers:
                return [visited_numbers[needed_number], i] #"Give me the index stored for number "need_number" "

            visited_numbers[nums[i]] = i # num : index