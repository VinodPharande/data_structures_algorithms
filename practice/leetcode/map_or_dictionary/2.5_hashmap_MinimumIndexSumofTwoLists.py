"""
Minimum Index Sum of Two Lists

Solution
Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.
A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order.


Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

Example 3:
Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
 

Constraints:
1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the strings of list1 are unique.
All the strings of list2 are unique.
There is at least a common string between list1 and list2.
"""

"""
Constraint Breakdown and How They Are Handled
Constraint	Where It Is Handled
1 <= len(list1), len(list2) <= 1000	✅ The O(n + m) complexity ensures that even for the maximum size (1000 elements), the solution runs efficiently.
1 <= len(word) <= 30	✅ Python’s string handling automatically supports words up to 30 characters. No need for explicit checks.
list1[i] and list2[i] consist of spaces and English letters	✅ Since Python dictionaries support string keys with spaces, this is naturally handled.
All strings in list1 are unique	✅ The dictionary {word: i for i, word in enumerate(list1)} ensures each string is stored only once, preventing duplicates.
All strings in list2 are unique	✅ The loop for j, word in enumerate(list2) iterates through unique values, so we never process duplicates.
There is at least one common string between list1 and list2	✅ No need for extra checks because the problem guarantees at least one common string.
"""



class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {}
        # # Store list1 in a hashmap
        for i, s in enumerate(list1):
            index_map[s] = i
            
            
        min_sum = float('inf')  # Initialize min index sum
        result = []

        for j, word in enumerate(list2):
            if word in index_map:  # If word is common
                index_sum = j + index_map[word]  # Compute index sum
                if index_sum < min_sum:  
                    min_sum = index_sum  # Update minimum sum
                    result = [word]  # Reset result list
                elif index_sum == min_sum:
                    result.append(word)  # Add to result if sum is equal

        return result  # Return words with minimum index sum
    

obj = Solution()
# res = obj.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) # Output: ["Shogun"]
# res = obj.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]) # Output: ["Shogun"]
res = obj.findRestaurant(["happy","sad","good"], ["sad","happy","good"]) # Output: ["sad","happy"]
print(res)
