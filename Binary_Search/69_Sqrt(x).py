#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def mySqrt(x):
    # We only need to search from 1 to x.
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        # If mid * mid is equal to x,
        # we found the exact square root.
        if mid * mid == x:
            return mid

        # If mid * mid is smaller than x,
        # we need a bigger number.
        elif mid * mid < x:
            left = mid + 1

        # If mid * mid is greater than x,
        # we need a smaller number.
        else:
            right = mid - 1

    # If x is not a perfect square,
    # right will contain the integer part of sqrt(x).
    return right


# Time Complexity: O(log x)
# Space Complexity: O(1)