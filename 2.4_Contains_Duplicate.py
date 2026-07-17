#ARRAY, HASHSET Contains Duplicate - EASY

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


#Optimized solution using HashSet (we're not using HashMap here because we don't need to count the frequency of elements, we just need to check for if the element is already present in the set or not)
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False
    
#TC: O(n)
#SC: O(n)

    
#Solved using HashMap ( not optimized)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ch in nums:
            count[ch] = count.get(ch, 0) + 1
        for i in range(len(nums)):
            if count[nums[i]] >= 2:
                return True
            return False
        
#Approach:
# Count the frequency of each element in the array using a HashMap.
# Traverse the array and return True if any element's frequency is greater than or equal to 2.
# Otherwise, return False.
#TC: O(n)   
#SC: O(n)