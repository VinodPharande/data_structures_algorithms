'''
 Intersection of Two Arrays

Solution
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
class Solution:
    '''custom implementation with set data structure'''
    # def intersection(self, nums1: [int], nums2: [int]) -> []:
    #     arr1 = set(nums1)
    #     print(f"arr1: {arr1}")
    #     arr2 = set(nums2)
    #     print(f"arr2: {arr2}")
    #     arr3 = []
    #     if 1 <= len(nums1) and len(nums2) <= 1000:
    #         for i1, val in enumerate(arr1):
    #             for i2, val2 in enumerate(arr2):
    #                 if 0 <= nums1[i1] and nums2[i2] <= 1000:
    #                     if val == val2:
    #                         arr3.append(val)
    #                     else:
    #                         pass
    #     return arr3

    '''implementation with set data structure'''
    def intersection(self, nums1: [int], nums2: [int]) -> []:
        # Apply Constraints
        if not (1 <= len(nums1) <= 1000 and 1 <= len(nums2) <= 1000):
            raise ValueError("Array lengths must be between 1 and 1000")
        if any(num < 0 or num > 1000 for num in nums1 + nums2):
            raise ValueError("Array elements must be between 0 and 1000")
        return list(set(nums1) & set(nums2))
        
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]        
solution = Solution()
result = solution.intersection(nums1, nums2)
print(result)  # Output: [9,4]