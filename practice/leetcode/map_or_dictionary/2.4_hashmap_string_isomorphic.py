"""
Isomorphic Strings

Solution
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) and 1 <= len(s) <= 5 * 10**4:  # Strings must be of equal length
            return False
    
        s_to_t = {}  # Mapping from s -> t
        t_to_s = {}  # Mapping from t -> s

        for char_s, char_t in zip(s, t):
            # print(f"char_s: {char_s}")
            # print(f"char_t: {char_t}")
            # Check if the mapping already exists
            if char_s in s_to_t:
                # print(f"if-1-char_s: {char_s}")
                # print(f"if-1-char_t: {char_t}")
                if s_to_t[char_s] != char_t:
                    return False  # Mismatch in mapping
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False  # Mismatch in reverse mapping
            else:
                t_to_s[char_t] = char_s

        return True  # If all checks pass, strings are isomorphic
        

obj = Solution()
# res = obj.isIsomorphic("egg", "add") # Output: True
res = obj.isIsomorphic("foo", "bar") # Output: False
# res = obj.isIsomorphic("paper", "title") # Output: True
print(f"res: {res}")