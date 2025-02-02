'''
Contains Duplicate

Solution
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    # def __init__(selfm, nums: [int]) -> None:
    #     self.nums = nums

    def containsDuplicate(self, nums:[int]) -> bool:
        seen = set() 
        # print(f"Info seen: {len(seen)}")

        for i, num in enumerate(nums):
            print(f"Info-i: {i}")
            if -10**9 <= nums[i] <= 10**9:
                # print(f"Info-1 num and seen: {num} and {seen}")
                # print(f"Info num: {num} and {seen}")
                if num in seen:
                    # print(f"inside if ")
                    return True
                seen.add(num)
        # print(f"Info-3 num and seen: {seen}")
        return False
    

    # Example Usage
# nums = [1, 2, 3, 4, 1] # Output: True
nums = [1,2,3,4] # Output: False
# nums =  [1,1,1,3,3,4,3,2,4,2] # Output: True
solution = Solution()
print(solution.containsDuplicate(nums))  