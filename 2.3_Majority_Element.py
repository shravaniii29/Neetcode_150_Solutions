#ARRAY, HASHMAP, Majority Element - EASY

#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for ch in nums:
            count[ch] = count.get(ch, 0) + 1
        for i in range(n):
            if count[nums[i]] > n/2:
                return nums[i]
            
#Approach:
# Count the frequency of each element in the array using a HashMap.
# Traverse the array and return the first element whose frequency is greater than n/2.
# Time Complexity: O(n)
# Space Complexity: O(n)