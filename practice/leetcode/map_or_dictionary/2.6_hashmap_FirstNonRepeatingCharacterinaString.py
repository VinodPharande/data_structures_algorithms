"""
Scenario II - Aggregate by Key
Report Issue
Another frequent scenario is to aggregate all the information by key. We can also use a hash map to achieve this goal.

An Example
Here is an example:
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
A simple way to solve this problem is to count the occurrence of each character first. And then go through the results to find out the first unique character.
Therefore, we can maintain a hashmap whose key is the character while the value is a counter for the corresponding character. Each time when we iterate a character, we just add the corresponding value by 1.

What's more
The key to solving this kind of problem is to decide your strategy when you encounter an existing key.
In the example above, our strategy is to count the occurrence. Sometimes, we might sum all the values up. And sometimes, we might replace the original value with the newest one. The strategy depends on the problem and practice will help you make a right decision.
"""

def aggregateByKey_or_firstUniqChar_hashmap(s):
    char_count = {}  # Step 1: Store character frequencies

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find first character with count == 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1  # No unique character found

# Test cases    
print(aggregateByKey_or_firstUniqChar_hashmap("leetcode"))  # 0
print(aggregateByKey_or_firstUniqChar_hashmap("loveleetcode"))  # 2
print(aggregateByKey_or_firstUniqChar_hashmap("aabb"))  # -1
print(aggregateByKey_or_firstUniqChar_hashmap("a"))  # 0
print(aggregateByKey_or_firstUniqChar_hashmap("ab"))  # 0
print(aggregateByKey_or_firstUniqChar_hashmap("aab"))  # 2
print(aggregateByKey_or_firstUniqChar_hashmap("aa"))  # -1
