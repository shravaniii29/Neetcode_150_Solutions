def nthRoot(n, x):
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        # Calculate mid^n
        value = mid ** n

        # If mid^n is exactly x,
        # mid is the exact nth root.
        if value == x:
            return mid

        # If mid^n is smaller than x,
        # we need a bigger value.
        elif value < x:
            left = mid + 1

        # If mid^n is greater than x,
        # we need a smaller value.
        else:
            right = mid - 1

    # right is the largest number
    # whose nth power is <= x.
    return right


# Time Complexity: O(log x)
# Space Complexity: O(1)