#Given a string s, find the length of the longest substring without duplicate characters.
#A substring is a contiguous sequence of characters within a string.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len

# Driver Code
s = input().strip()
print(lengthOfLongestSubstring(s)) #u dont need to make a class in TCS-like test formats, just start from def func name, and dont forget to add this driver code at the end of your code, otherwise it will give runtime error.
    
# Approach:
        # - Use a sliding window with two pointers (left, right).
        # - Maintain a set containing unique characters in the current window.
        # - Expand the window by moving 'right'.
        # - If a duplicate character is found, shrink the window from the left
        #   until the duplicate is removed.
        # - Update the maximum window size after each expansion.

        # Time Complexity: O(n)
        # - Each character is added and removed from the set at most once.

        # Space Complexity: O(min(n, charset))
        # - In the worst case, the set stores all unique characters.
        
# VISUALISATION:
# | Right | Char | Duplicate? | Left After | Current Window | Max |
# | ----: | ---- | ---------- | ---------: | -------------- | --: |
# |     0 | z    | No         |          0 | z              |   1 |
# |     1 | x    | No         |          0 | zx             |   2 |
# |     2 | y    | No         |          0 | zxy            |   3 |
# |     3 | z    | Yes        |          1 | xyz            |   3 |
# |     4 | x    | Yes        |          2 | yzx            |   3 |
# |     5 | y    | Yes        |          3 | zxy            |   3 |
# |     6 | z    | Yes        |          4 | xyz            |   3 |