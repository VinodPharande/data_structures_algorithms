'''
Find Duplicates By Hash Set

As we know, it is easy and effective to insert a new value and check if a value is in a hash set or not.
Therefore, typically, a hash set is used to check if a value has ever appeared or not.
 
An Example
Let's look at an example:
Given an array of integers, find if the array contains any duplicates. 
This is a typical problem which can be solved by a hash set.
You can simply iterate each value and insert the value into the set. If a value has already been in the hash set, there is a duplicate.
'''

def contains_duplicate(nums):
    seen = set()
    print(f"Info seen: {len(seen)}")
    
    for i, num in enumerate(nums):
        if -10**9 <= nums[i] <= 10**9:
            print(f"Info-1 num and seen: {num} and {seen}")
            print(f"Info num: {num} and {seen}")
            if num in seen:
                print(f"inside if ")
                return True
            seen.add(num)
    print(f"Info-3 num and seen: {seen}")
    return False

# Example Usage
nums = [1, 2, 3, 4, 1]
# nums = [1,2,3,4]
# nums =  [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))  # Output: True