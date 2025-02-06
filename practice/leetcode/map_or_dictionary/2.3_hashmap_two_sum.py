"""
Two Sum

Solution
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:

    '''using enumerate function'''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}  # Dictionary to store number and its index
        if 2 <= len(nums) <= 10**4:
            for index, num in enumerate(nums):
                if -10**9 <= nums[index] <= 10**9 and -10**9 <= target <= 10**9:
                    complement = target - num  # Find the number needed to reach target
                    if complement in hash_map:  # Check if complement exists
                        return [hash_map[complement], index]  # Return indices
                    hash_map[num] = index  # Store number and index
            return []  # This should never be reached as per problem statement

    # '''using range function'''
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     print(f": {nums}")
    #     # create a dictionary to store the values
    #     dict = {}
    #     # iterate over the list
    #     for i in range(len(nums)):
    #         # check if the target - current element is in the dictionary
    #         print(f"[i]: {i}")
    #         print(f"target: {target - nums[i]}")
    #         if (target - nums[i]) in dict:
    #             # return the index of the element in the dictionary and the current element
    #             print(f"inside if: {dict[target - nums[i]]}, {i}")
    #             return [dict[target - nums[i]], i]
    #         # add the element to the dictionary
    #         dict[nums[i]] = i
    #     return dict

# test the solution
obj = Solution()
res = obj.twoSum([2,7,11,15], 9) # [0, 1]
# obj.twoSum([3,2,4], 6) # [1, 2]
# obj.twoSum([3,3], 6) # [0, 1]
print(f"final result: {res}")

