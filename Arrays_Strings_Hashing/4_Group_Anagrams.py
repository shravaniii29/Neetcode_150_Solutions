from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            key = "".join(sorted(word)) #sorted() returns a LIST. Not a string. 'join' joins the letters back together.

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())

    # Driver Code
    n = int(input().strip())
    strs = input().split() #because strs in an array of strings and not integers ( thts why we didnt do 'list(map(int, input().split()))'  )
    print(groupAnagrams(strs))


# Approach:
# Sort every word.
# Words with the same sorted form are anagrams.
# Use the sorted word as the dictionary key and
# store all matching words in the same list.
#
# Time Complexity: O(n × k log k)
# Space Complexity: O(n × k)
#
# n = number of strings
# k = average length of each string