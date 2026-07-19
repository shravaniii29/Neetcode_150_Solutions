class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        # Count frequency of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Store frequencies in a set
        freq_set = set(freq.values())

        # Compare sizes
        return len(freq) == len(freq_set)


        # Approach:
        # 1. Count the frequency of every number using a hash map.
        # 2. Store all the frequencies in a hash set.
        # 3. If two numbers have the same frequency, the set size
        #    will be smaller than the dictionary size.
        # 4. Return True if all frequencies are unique.
        #
        # Time Complexity:
        # O(n)
        # - O(n) to count frequencies.
        # - O(k) to insert frequencies into the set.
        #
        # Space Complexity:
        # O(k)
        # - Hash map stores k unique numbers.
        # - Hash set stores their frequencies.