#Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#Return the minimum integer k such that she can eat all the bananas within h hours.



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We are searching for the minimum possible eating speed k.
        # Minimum speed can be 1 banana/hour.
        left = 1

        # Maximum speed needed is the largest pile.
        # At this speed, Koko can finish any pile in at most 1 hour.
        right = max(piles)

        # Binary search for the smallest valid speed.
        while left < right:

            # Try the middle eating speed.
            mid = (left + right) // 2

            # Calculate how many hours Koko needs at this speed.
            hours = 0

            # Check every banana pile.
            for pile in piles:
                # ceil(pile / mid) = (pile + mid - 1) // mid
                # This tells us how many hours are needed for this pile.
                hours += (pile + mid - 1) // mid

            # If she can finish within h hours,
            # mid is a possible answer, so try a smaller speed.
            if hours <= h:
                right = mid

            # If she needs more than h hours,
            # mid is too slow, so we need a faster speed.
            else:
                left = mid + 1

        # left is the smallest speed that allows her to finish in h hours.
        return left
    
# Time Complexity: O(n * log(max(piles)))
# n = number of piles
# Binary search takes O(log(max(piles))) iterations,
# and each iteration checks all n piles.

# Space Complexity: O(1)
# We only use a few variables (left, right, mid, hours).