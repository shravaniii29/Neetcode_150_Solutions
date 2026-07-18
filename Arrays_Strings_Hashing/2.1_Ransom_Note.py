#ARRAY, HASHMAP, Counting Chars in strings - EASY
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        count = {}

        # Count characters in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Use characters for ransomNote
        for ch in ransomNote:

            if count.get(ch, 0) == 0:
                return False

            count[ch] -= 1

        return True

# Approach:
# Count the frequency of each character in the magazine using a HashMap.
# Traverse the ransomNote and consume one occurrence of each character.
# If any required character is unavailable, return False.
# Otherwise, return True.
#
# Time Complexity: O(n + m)
# Space Complexity: O(k)
# where k is the number of distinct characters.