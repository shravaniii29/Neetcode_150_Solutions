class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_numbers = {} # val : index

        for i in range(len(nums)):
            needed_number = target - nums[i]

            if needed_number in visited_numbers:
                return [visited_numbers[needed_number], i]

            visited_numbers[nums[i]] = i #val : index