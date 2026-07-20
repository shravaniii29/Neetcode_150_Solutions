# STRING QUESTION
# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order. (Lexicographical order is the order in which words appear in a dictionary; for example, "apple" comes before "banana".)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {}

        # Count frequency
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        # Sort by frequency(desc), then word(asc)
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0])) #Negative frequency for descending order, word for ascending order. 
        #Negative frequency is used to sort in descending order because Python's sorted function sorts in ascending order by default. Negative values mein -2 is less than -1, so it will come first in the sorted order, effectively giving us a descending sort based on frequency. 

        ans = []

        for word, count in sorted_words[:k]:
            ans.append(word)

        return ans
    
    
# Approach:
        # 1. Count frequency of every word using a hash map.
        # 2. Sort the (word, frequency) pairs:
        #       - Higher frequency first.
        #       - If frequencies are equal, alphabetical order.
        # 3. Return the first k words.
        #
        # Time Complexity:
        # O(n + m log m)
        # n = total number of words
        # m = number of unique words
        #
        # Space Complexity:
        # O(m)