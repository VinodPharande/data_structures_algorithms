'''
Hash Map - Usage
Report Issue
The hash map is one of the implementations of a map which is used to store (key, value) pairs.

We provide an example of using the hash map in Java, C++ and Python. If you are not familiar with the usage of the hash map, it will be helpful to go through the example.
'''

# 1. initialize a hash map
hashmap = {'key_0' : 'val_0', 'key_2' : 'val_3'}

# 2. insert a new (key, value) pair or update the value of existed key
hashmap['key_1'] = 'val_1'
# hashmap['key_1'] = 'val_2'

# 3. get the value of a key
print("The value of key_1 is: " + str(hashmap['key_1']))

# 4. delete a key
del hashmap['key_2']

# 5. check if a key is in the hash map
if 'key_2' not in hashmap:
    print("'key_2' is not in the hash map.")

# 6. both key and value can have different type in a hash map
hashmap["pi"] = 3.1415

# 7. get the size of the hash map
print("The size of hash map is: " + str(len(hashmap)))

# 8. iterate the hash map
for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("are in the hash map.")

# 9.1 get all keys in hash map
print(hashmap.keys())
# 9.2 get all values in hash map
print(hashmap.values())
# 9.3 get all items in hash map
print(hashmap.items())

# 10. clear the hash map
hashmap.clear();
print("The size of hash map is: " + str(len(hashmap)))
