#String, Hash Table EASY

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in s_to_t:
                if s_to_t[ch1] != ch2:
                    return False
            else:
                s_to_t[ch1] = ch2


            if ch2 in t_to_s:
                if t_to_s[ch2] != ch1:
                    return False
            else:
                t_to_s[ch2] = ch1
        return True

#Approach:
# Use two HashMaps to maintain the mapping between characters in s and t.
# Traverse the strings simultaneously, checking for consistency in the mappings.
# If any inconsistency is found, return False. Otherwise, return True.
# Time Complexity: O(n)
# Space Complexity: O(n)