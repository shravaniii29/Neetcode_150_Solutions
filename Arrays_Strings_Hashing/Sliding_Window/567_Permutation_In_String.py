#Strin, Sliding Window, Hash Map - Medium
#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

#In other words, return true if one of s1's permutations is the substring of s2.



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:



        if len(s1) > len(s2):
            return False

        s1_count = {}
        window = {}

        # Frequency of s1
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add current character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):

                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # Compare frequencies
            if window == s1_count:
                return True

        return False
            
            
            
# Approach:
        # 1. Store the frequency of characters in s1.
        # 2. Create a sliding window of size len(s1) over s2.
        # 3. Maintain the frequency of the current window.
        # 4. Compare both frequency maps.
        #    If they match, a permutation exists.
        #
        # Time Complexity:
        # O(n)
        #
        # Space Complexity:
        # O(1)
        # (Only lowercase English letters → at most 26 characters)