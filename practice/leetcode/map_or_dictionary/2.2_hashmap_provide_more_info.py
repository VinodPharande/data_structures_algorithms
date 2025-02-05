'''
Scenario I - Provide More Information
Report Issue
The first scenario to use a hash map is that we need more information rather than only the key. Then we can build a mapping relationship between key and information by hash map.
 

An Example
Let's look at an example:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

In this example, if we only want to return true if there is a solution, we can use a hash set to store all the values when we iterate the array and check if target - current_value is in the hash set or not.

However, we are asked to return more information which means we not only care about the value but also care about the index. 

`We need to store not only the number as the key but also the index as the value. Therefore, we should use a hash map rather than a hash set.`

What's More
In some cases, we need more information not just to return more information but also to help us with our decisions.
In the previous examples, when we meet a duplicated key, we will return the corresponding information immediately. But sometimes, we might want to check if the value of the key is acceptable first.
'''


def find_duplicates(nums):
    # Initialize an empty dictionary to store the number and its index i.e. key-value pair
    # hash_map = {number: index} i.e. number will be key and index will be value
    # it is bit tricky to understand the key-value pair in this context
    # but it is the best way to store the number and its index
    # because key can not be duplicated and value can be duplicated, as in this example we are constructing hash_map from array
    hash_map = {}
    duplicates = []
    
    # Iterate over the list
    print(f"Info nums: {nums}")
    
    for value, key in enumerate(nums):
        print(f"Info hash_map-{value} and {key}: {hash_map}")
        if key in hash_map:
            # If the number is already in the hash_map, it's a duplicate
            # key is the number and value is the index
            duplicates.append((value, key, hash_map[key]))
        else:
            # If it's not in the hash_map, store the number with its key i.e. key-value pair
            # insert a new (key, value) pair
            # e.g. hashmap['key_1'] = 'val_1'
            hash_map[key] = value
            print(f"Info value and hash_map: {key} and {hash_map}")
        print(f"********************************")
    return duplicates

# Example usage
# index 0   1   2   3   4   5
nums = [10, 20, 30, 10, 40, 20]
duplicates = find_duplicates(nums)
print(f"duplicates: {duplicates}")

# Output duplicates
for value, current_index, previous_index in duplicates:
    print(f"Duplicate value {current_index} found at index {value}, previously at index {previous_index}")
