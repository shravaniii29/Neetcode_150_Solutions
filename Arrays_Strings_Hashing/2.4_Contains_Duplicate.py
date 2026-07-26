#ARRAY, HASHSET Contains Duplicate - EASY

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


#Optimized solution using HashSet (we're not using HashMap here because we don't need to count the frequency of elements, we just need to check for if the element is already present in the set or not)
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
    # Driver Code
    n = int(input().strip()) #Reads the size of the array.

    nums = list(map(int, input().split()))

    print(containsDuplicate(nums))
    
    
#TC: O(n)
#SC: O(n)

    
#Solved using HashMap ( not optimized)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ch in nums:
            count[ch] = count.get(ch, 0) + 1
        for i in range(len(nums)):
            if count[nums[i]] >= 2:
                return True
            return False
        
#Approach:
# Count the frequency of each element in the array using a HashMap.
# Traverse the array and return True if any element's frequency is greater than or equal to 2.
# Otherwise, return False.
#TC: O(n)   
#SC: O(n)



#JAVA:
# import java.util.*;

# public class Main {

#     // Approach:
#     // 1. Create a HashSet to store the elements we've already seen.
#     // 2. Traverse the array.
#     // 3. If the current element already exists in the HashSet,
#     //    a duplicate is found, so return true.
#     // 4. Otherwise, add the element to the HashSet.
#     //
#     // Time Complexity: O(n)
#     // - Each HashSet operation (contains/add) takes O(1) on average.
#     //
#     // Space Complexity: O(n)
#     // - In the worst case, all elements are unique and stored in the HashSet.

#     public static boolean containsDuplicate(int[] nums) {

#         HashSet<Integer> seen = new HashSet<>();

#         for (int num : nums) {

#             if (seen.contains(num)) {
#                 return true;
#             }

#             seen.add(num);
#         }

#         return false;
#     }

#     public static void main(String[] args) {

#         Scanner sc = new Scanner(System.in);

#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         System.out.println(containsDuplicate(nums));

#         sc.close();
#     }
# }