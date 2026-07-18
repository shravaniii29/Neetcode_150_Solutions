#ARRAY, STRING, HASHMAP, Counting Chars in strings - EASY
#You are given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
# Approach:
# Count the frequency of each character using a HashMap.
# Traverse the string again and return the index of the
# first character whose frequency is 1.
# If no such character exists, return -1.
#
# Time Complexity: O(n)
# Space Complexity: O(n)