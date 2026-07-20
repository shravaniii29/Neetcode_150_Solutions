#ARRAY, HASHMAP, Sliding Window - EASY

#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}

        for i in range(len(nums)):
            if nums[i] in indexMap:
                if i - indexMap[nums[i]] <= k:
                    return True
            
            indexMap[nums[i]] = i
        return False



# Approach:
# Use a HashMap to store the last index where each number appeared.
# If the current number has appeared before, check whether the
# difference between the current index and the previous index is <= k.
# If yes, return True. Otherwise, update its latest index.
#
# Time Complexity: O(n)
# Space Complexity: O(n)