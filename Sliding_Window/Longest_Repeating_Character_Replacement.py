#You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Approach:
        # - Use Sliding Window.
        # - Keep the frequency of characters in the current window.
        # - max_freq stores the highest frequency character.
        # - If characters to replace > k, shrink the window.
        # - Keep track of the largest valid window.

        # Time Complexity: O(n)
        # Space Complexity: O(26) = O(1)

        freq = {}

        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:

                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len