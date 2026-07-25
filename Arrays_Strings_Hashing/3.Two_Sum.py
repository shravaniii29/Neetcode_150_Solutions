#Given an array of integers 'nums' and an integer 'target', return the indices i and j such that nums[i] + nums[j] == target and i != j.

#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_numbers = {} # num : index

        for i in range(len(nums)):
            needed_number = target - nums[i]

            if needed_number in visited_numbers:
                return [visited_numbers[needed_number], i] #"Give me the index stored for number "need_number" "

            visited_numbers[nums[i]] = i # num : index
            
#JAVA:
# import java.util.*;

# public class Main {

#     // Approach:
#     // 1. Store each visited number and its index in a HashMap.
#     // 2. For every number, calculate the required complement.
#     // 3. If the complement already exists in the HashMap,
#     //    return the two indices.
#     // 4. Otherwise, store the current number and its index.
#     //
#     // Time Complexity: O(n)
#     // Space Complexity: O(n)

#     public static int[] twoSum(int[] nums, int target) {

#         HashMap<Integer, Integer> map = new HashMap<>();

#         for (int i = 0; i < nums.length; i++) {

#             int needed = target - nums[i];

#             if (map.containsKey(needed)) {
#                 return new int[]{map.get(needed), i};
#             }

#             map.put(nums[i], i);
#         }

#         return new int[]{-1, -1};
#     }

#     public static void main(String[] args) {

#         Scanner sc = new Scanner(System.in);

#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         int target = sc.nextInt();

#         int[] ans = twoSum(nums, target);

#         System.out.println(ans[0] + " " + ans[1]);

#         sc.close();
#     }
# }