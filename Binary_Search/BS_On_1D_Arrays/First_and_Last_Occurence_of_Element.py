#Solved using Lower Bound and Upper Bound (Binary Search)
def lower_bound(arr, x): #x => target element to be searched
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            right = mid
        else:
            left = mid + 1

    return left


def upper_bound(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > x:
            right = mid
        else:
            left = mid + 1

    return left


def first_last(arr, x):
    lb = lower_bound(arr, x)

    if lb == len(arr) or arr[lb] != x:
        return [-1, -1]

    ub = upper_bound(arr, x)

    return [lb, ub - 1]


arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

print(first_last(arr, x))