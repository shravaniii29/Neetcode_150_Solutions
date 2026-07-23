#Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring.
# If such a substring does not exist, return an empty string "".

#You may assume that the correct output is always unique.



from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:


        if len(t) > len(s):
            return ""

        tCount = Counter(t)
        window = {}

        have = 0
        need = len(tCount)

        left = 0

        res = [-1, -1]
        minLen = float("inf")

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in tCount and window[ch] == tCount[ch]:
                have += 1

            while have == need:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1

                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l:r+1] if minLen != float("inf") else ""
    
# Approach:
        # 1. Store frequency of characters in t.
        # 2. Expand the window using the right pointer.
        # 3. Track how many characters satisfy the required frequency.
        # 4. Once all required characters are matched,
        #    shrink the window from the left.
        # 5. Keep updating the minimum window.

        # Time Complexity: O(n)
        # Each character is visited at most twice
        # (once by right pointer and once by left pointer).

        # Space Complexity: O(m)
        # m = number of unique characters in t.