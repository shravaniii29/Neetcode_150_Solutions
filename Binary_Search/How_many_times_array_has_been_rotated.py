def findRotations(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the rightmost element,
        # the minimum element (rotation point) must be on the right side.
        if nums[mid] > nums[right]:
            left = mid + 1

        # Otherwise, the minimum element is at mid
        # or somewhere on the left side.
        else:
            right = mid

    # left now points to the index of the minimum element.
    # The index of the minimum element = number of rotations.
    return len(nums) - left # -> this is for left rotation, if you want to do for right rotation then 'return left'


# Time Complexity: O(log n)
# Space Complexity: O(1)