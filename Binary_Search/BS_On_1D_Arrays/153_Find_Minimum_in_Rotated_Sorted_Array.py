def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the rightmost element,
        # the minimum must be on the right side.
        if nums[mid] > nums[right]:
            left = mid + 1

        # Otherwise, the minimum is at mid or somewhere on the left.
        else:
            right = mid

    # left == right, so we've found the minimum element.
    return nums[left]


# Time Complexity: O(log n)
# Space Complexity: O(1)