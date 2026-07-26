#STRING Question

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        #Creating two empty dictionaries
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #if the char doesn't exist in the dict, 'get' will return 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
            #This is why .get(key, 0) is so useful—it avoids checking whether the key already exists.

        return countS == countT
    
    # Driver Code (Don't forget to add this when blank terminal is given - like TCS)
    s = input().strip()
    t = input().strip()

    print(isAnagram(s, t))


# Approach:
# If the lengths are different, they cannot be anagrams.
# Count the frequency of each character in both strings.
# If both frequency dictionaries are identical, return True.
# Otherwise, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)