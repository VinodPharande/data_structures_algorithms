"""
Contains Duplicate II

Solution
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105


In simple terms, you need to find duplicate values that appear close enough in the array 
(within a distance of k indices).

Example 1:
nums = [1, 2, 3, 1]
k = 3
Explanation:
The value 1 appears at index 0 and index 3 in the array.
The absolute difference of indices is |0 - 3| = 3, which is less than or equal to k.
Since there is a duplicate with indices that satisfy the condition, the output is True.
Output:
True

Example 2:
nums = [1, 2, 3, 1, 2, 3]
k = 2
Explanation:
The value 1 appears at indices 0 and 3. The absolute difference is |0 - 3| = 3, which is greater than k (3 > 2). So this pair doesn't count.
The value 2 appears at indices 1 and 4. The absolute difference is |1 - 4| = 3, which is greater than k (3 > 2). This doesn't count either.
The value 3 appears at indices 2 and 5. The absolute difference is |2 - 5| = 3, which is greater than k (3 > 2).
Since no duplicates satisfy the condition, the output is False.
Output:
False

Example 3:
nums = [1, 0, 1, 1]
k = 1
We are given:

An array of integers: nums = [1, 0, 1, 1]
A number k = 1, which means we are looking for two distinct indices i and j such that:
nums[i] == nums[j] (the values at both indices are the same).
The absolute difference of the indices |i - j| <= k.
We want to check if there are any duplicate elements in the array, and if so, whether the distance between the indices is less than or equal to k.

Step-by-Step Breakdown:
First element: nums[0] = 1
We haven't seen the value 1 before, so we store its index in the hash map.
Hash map: {1: 0} (this means 1 is seen at index 0).

Second element: nums[1] = 0
We haven't seen the value 0 before, so we store its index in the hash map.
Hash map: {1: 0, 0: 1} (this means 0 is seen at index 1).

Third element: nums[2] = 1
We have seen the value 1 before (at index 0).
Now, we check if the absolute difference between the current index (i = 2) and the last seen index of 1 (j = 0) is <= k.
|2 - 0| = 2
Since 2 > k (i.e., 2 > 1), the distance is too large, so we do not count this pair.
We update the hash map to store the most recent index of 1.
Hash map: {1: 2, 0: 1} (the value 1 is now stored at index 2).

Fourth element: nums[3] = 1
We have seen the value 1 before (at index 2).
We check if the absolute difference between the current index (i = 3) and the last seen index of 1 (j = 2) is <= k.
|3 - 2| = 1
Since 1 <= k (i.e., 1 <= 1), the distance is valid, and we count this pair.
At this point, we found a pair of indices (2, 3) that satisfy the condition:
nums[2] == nums[3] = 1
|2 - 3| = 1 <= k
Since we found a duplicate with an index difference less than or equal to k, we return True.

Final Output:
True
"""

class Solution:
    
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the last seen index of each element
        seen = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Check if the current number has been seen before and the index difference is <= k
            # if num in seen and i - seen[num] <= k:
            #     return True  # Found a duplicate within the required range
            '''simpler code of above map comprehension'''
            if num in seen:
                print(f"num: {num}")
                # seen[num] is j
                if i - seen[num] <= k:
                    print(f"i: {i}, num: {num}, seen[num]: {seen[num]}")
                    print(f"i - seen[num]: {i - seen[num]}")
                    return True  # Found a duplicate within the required range
            
            # Update the last seen index of the current number
            print(f"directly to seen: {seen}")
            seen[num] = i
        
        # If no such duplicate is found, return False
        return False

# Example usage:
obj = Solution()
nums = [1, 0, 1, 1]
k = 1
print(obj.containsNearbyDuplicate(nums, k))  # Output: True