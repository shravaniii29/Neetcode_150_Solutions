#ARRAY PROBLEM - EASY
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #here 0 is the default value if the key does not exist in the dictionary, so it will return 0 and then add 1 to it, effectively counting the occurrences of each character in the string s.
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT # => This will return True if both dictionaries are identical, meaning that both strings have the same characters with the same frequency, and False otherwise.


# Approach:
# If the lengths are different, they cannot be anagrams.
# Count the frequency of each character in both strings.
# If both frequency dictionaries are identical, return True.
# Otherwise, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)