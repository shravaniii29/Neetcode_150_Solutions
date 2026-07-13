# Time Complexity: O(n)
# - First pass (left products): O(n)
# - Second pass (right products): O(n)
# Overall: O(n)

# Space Complexity: O(1) extra space
# (Ignoring the output array as per LeetCode convention)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Result array initialized with 1s
        res = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix product
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res