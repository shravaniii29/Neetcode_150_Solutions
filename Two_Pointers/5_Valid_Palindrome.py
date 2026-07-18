class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] != s[j]:
                return False
            i += 1
        return True