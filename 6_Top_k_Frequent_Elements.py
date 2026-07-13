# Time Complexity: O(n)
# - Counting frequencies: O(n)
# - Placing elements into buckets: O(n)
# - Traversing buckets: O(n)
# Overall: O(n)

# Space Complexity: O(n)
# - Frequency dictionary: O(n)
# - Bucket list: O(n)
# - Result list: O(k) <= O(n)
# Overall: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Dictionary to store the frequency of each number
        count = {}

        # Bucket list where index = frequency
        # Maximum possible frequency = len(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        # Count the frequency of each element
        for num in nums:
            count[num] = 1 + count.get(num, 0) #count.get(num, 0) => "If key 'num' exists, give me its value. Otherwise, give me 0.". If we dont use get() and only use count[num], python would throw a KeyError

        # Place each number into its corresponding frequency bucket
        for num, c in count.items(): #count.items() gives (number, frequency)
            freq[c].append(num) #Put each number into the bucket corresponding to its frequency.

        # Store the final answer
        res = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                # Stop once we have collected k elements
                if len(res) == k:
                    return res

# Why not just use count?
# Because count is organized as => Number → Frequency
# But we actually need => Frequency → Numbers

# That's exactly what freq gives us.


