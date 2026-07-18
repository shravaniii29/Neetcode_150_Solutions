class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT


# Approach:
# If the lengths are different, they cannot be anagrams.
# Count the frequency of each character in both strings.
# If both frequency dictionaries are identical, return True.
# Otherwise, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)