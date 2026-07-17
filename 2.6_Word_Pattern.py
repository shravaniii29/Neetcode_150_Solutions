#ARRAY, HASHMAP, Mapping Chars in strings - EASY

#Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        ctw = {} #ctw => char to word
        wtc = {} #wtc => word to char

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in ctw:
                if ctw[ch] != word:
                    return False
            else:
                ctw[ch] = word

            if word in wtc:
                if wtc[word] != ch:
                    return False
            else:
                wtc[word] = ch

        return True
    
#Approach :
# Use two HashMaps to maintain the mapping between characters in pattern and words in s.
# Traverse the pattern and words simultaneously, checking for consistency in the mappings.
# If any inconsistency is found, return False. Otherwise, return True.
#TC: O(n)   
#SC: O(n)