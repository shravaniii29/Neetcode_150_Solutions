#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        # For x = 0 or 1, the answer is x itself.
        if x < 2:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2

            # If mid * mid is equal to x,
            # we found the exact square root.
            if mid * mid == x:
                return mid

            # If mid * mid is smaller than x,
            # we need to search on the right side.
            elif mid * mid < x:
                left = mid + 1

            # If mid * mid is greater than x,
            # we need to search on the left side.
            else:
                right = mid - 1

        # If x is not a perfect square,
        # right will contain the integer part of sqrt(x).
        return right # because left ends up pointing at the first place that is not possible and right ends up pointing at the last place that is possible. So we return right.


# Time Complexity: O(log n)
# Space Complexity: O(1)

# Key idea: We're looking for the largest number mid such that mid² ≤ x.