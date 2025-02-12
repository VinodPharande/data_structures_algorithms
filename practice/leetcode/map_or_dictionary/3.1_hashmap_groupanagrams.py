"""
Group Anagrams

Solution
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    '''Custom hash function to group anagrams'''
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}  # Regular dictionary to store anagram groups.
    
        for word in strs:
            # Sort the word and use the sorted string as the key.
            sorted_word = ''.join(sorted(word))
            print(f"sorted_Word-1: {sorted_word}")
            # # If the key doesn't exist, initialize it with an empty list.
            if sorted_word not in anagram_map:
                print(f"inside sorted_Word: {sorted_word}")
                anagram_map[sorted_word] = []

            # Append the original word to the appropriate list.
            anagram_map[sorted_word].append(word)

        # Return the grouped anagrams.
        return list(anagram_map.values())
    
    '''built-in hash function to group anagrams'''
    # from collections import defaultdict
    # def groupAnagrams(strs):
    #     anagram_map = defaultdict(list)  # Create a defaultdict where the default value is a list.
        
    #     for word in strs:
    #         sorted_word = ''.join(sorted(word))  # Sort the word and convert it back to a string.
    #         anagram_map[sorted_word].append(word)  # Add the original word to the anagram group.
        
    #     return list(anagram_map.values())  # Return the list of values from the hashmap.


obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]