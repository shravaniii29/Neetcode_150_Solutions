#Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.


from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        pCount = Counter(p)
        window = Counter()

        left = 0
        ans = []

        for right in range(len(s)):

            # Add current character
            window[s[right]] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Compare frequencies
            if window == pCount:
                ans.append(left)

        return ans

# Approach:
        # 1. Store the frequency of characters in p.
        # 2. Use a sliding window of size len(p) over s.
        # 3. Add the current character to the window.
        # 4. If the window becomes larger than len(p), remove the leftmost character.
        # 5. Whenever the window frequency matches p's frequency,
        #    the current window is an anagram, so store its starting index.
        #
        # Time Complexity: O(n)
        # - We traverse s once using the sliding window.
        # - Counter comparison is O(26) (constant) since only lowercase English letters exist.
        #
        # Space Complexity: O(1)
        # - We use two Counter objects storing at most 26 lowercase letters.
