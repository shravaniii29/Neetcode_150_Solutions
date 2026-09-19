#MOST BASIC BINARY SEARCH APPLICATION
#Target will be given, you have to find the index of that target in the given array, if the element is not present in the array return -1


a = [1,2,3,4,5,6,7,8]
target = 9
left = 0
right = len(a)-1

while left <= right:
    mid = (left + right)//2
    
    if a[mid]==target:
        print("Target was " , a[mid] , ', Index:' , mid)
        break
    elif a[mid] > target:
        right = mid - 1
    else:
        left = mid +1
        
else:
    print(-1)
        
#------------------------------------------------------------------
        
#TO PERFORM THE SAME USING RECURSION

a = [1, 2, 3, 4, 5, 6, 7, 8]
target = 7

def binary_search(a, left, right, target):

    if left > right: #As soon as left becomes greater than right, it means the target is not present in the array
        return -1

    mid = (left + right) // 2

    if a[mid] == target:
        return a[mid]

    elif a[mid] > target:
        return binary_search(a, left, mid - 1, target)

    else:
        return binary_search(a, mid + 1, right, target)


ans = binary_search(a, 0, len(a) - 1, target)
print(ans)
