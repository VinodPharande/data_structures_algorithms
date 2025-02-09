"""
Intersection of Two Arrays i.e. common elements in both arrays

Solution
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 
Constraints: 
[These conditions are implicitly implemented by python i.e. by default by below code]
[or we can even explicitly implement using if conditions in code below]
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Step 1: Create a dictionary to count occurrences in nums1
        counts = {}  # Explicitly writing the Counter logic
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        # e.g. {1: 2, 2: 2}
        print(f"Counts: {counts}")

        # Step 2: Iterate through nums2 and check for common elements
        result = []
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1  # Reduce count after adding to result
                print(f"Reduced Counts: {counts}")

        return result
    
    '''Two Pointers approach algorithm for sorted arrays'''
    # def intersect_sorted(nums1, nums2):
    #     nums1.sort()  # Ensure sorted (if not already sorted)
    #     nums2.sort()
        
    #     i, j = 0, 0
    #     result = []
        
    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         elif nums1[i] > nums2[j]:
    #             j += 1
    #         else:  # Found common element
    #             result.append(nums1[i])
    #             i += 1
    #             j += 1
        
    #     return result

    '''What if nums2 is stored on disk and we have limited memory?
    Use the "Stream Processing" or "Chunk Processing" Approach
    Read nums2 in chunks and process it in chunks'''
    # def intersect_disk(nums1, nums2_stream):
    #     counts = {}  # Store nums1 in memory
    #     for num in nums1:
    #         counts[num] = counts.get(num, 0) + 1

    #     result = []
        
    #     # Process nums2 in chunks (simulating disk read)
    #     for chunk in nums2_stream:  # Assuming nums2_stream yields chunks of nums2
    #         for num in chunk:
    #             if num in counts and counts[num] > 0:
    #                 result.append(num)
    #                 counts[num] -= 1
        
    #     return result
    
# Time complexity: O(n + m) where n and m are the lengths of the input arrays   
# Space complexity: O(min(n, m)) to store the counts dictionary
obj = Solution()    
print(obj.intersect([1,2,2,1], [2,2]))  # [2,2]
# print(obj.intersect([4,9,5], [9,4,9,8,4]))  # [4,9]
# print(obj.intersect([1,2,2,1], [2]))  # [2]
# print(obj.intersect([1,2,2,1], [2,2,2]))  # [2,2]
# print(obj.intersect([1,2,2,1], [2,2,2,2]))  # [2,2]

# More test cases




