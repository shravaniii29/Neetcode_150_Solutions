#ARRAY, HASHTABLE, FREQUENCY Medium Question - Sender With Largest Word Count

#You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

# A message is list of words that are separated by a single space with no leading or trailing spaces. 
# The word count of a sender is the total number of words sent by the sender. 
# Note that a sender may send more than one message.
# Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.

# Note:
# Uppercase letters come before lowercase letters in lexicographical order.
# "Alice" and "alice" are distinct

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        freq = {}

        # Count total words for each sender
        for i in range(len(messages)):
            words = len(messages[i].split())
            sender = senders[i]

            freq[sender] = freq.get(sender, 0) + words

        max_words = 0
        ans = ""

        # Find sender with highest word count
        for sender, count in freq.items(): #freq.items() returns both the key and value of the dictionary ( other built-in methods are freq.keys(), freq.values(), freq.get(), freq.pop(), freq.clear(), freq.update() )

            if count > max_words:
                max_words = count
                ans = sender

            elif count == max_words:
                ans = max(ans, sender) #because we want the lexicographically larger name in case of a tie, we use the max function to compare the current answer with the new sender.(larger in lexicographical order means the one that would come later in a dictionary or alphabetical list.)

        return ans
    
# Approach:
        # 1. Traverse both arrays together.
        # 2. Count the number of words in each message.
        # 3. Store the total word count for each sender.
        # 4. Find the sender with the maximum word count.
        #    If there is a tie, return the lexicographically larger name.
        #
        # Time Complexity:
        # O(n * m)
        # n = number of messages
        # m = average number of words in a message
        #
        # Space Complexity:
        # O(k)
        # k = number of unique senders
        
