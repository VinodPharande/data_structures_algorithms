
'''
Design HashMap

Solution
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the myHashMapect with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); # The map is now [[1,1]]
myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]
'''

'''
Implementation using python "list" collection which is a dynamic array instead of linked list
because linked list requires extra space for pointers and also it is slower than dynamic array.
'''
class MyHashMap:

    # initialize your data structure here.
    def __init__(self, initial_size=1, load_factor_threshold=0.7):
        self.size = 10
        self.load_factor_threshold = load_factor_threshold
        self.num_elements = 0  # Tracks the number of stored elements
        '''separate chaining this for resolution of collision i.e. too many keys, mapping to same index'''
        self.buckets = [[] for _ in range(self.size)]

    '''automatically resize the array i.e. self.size, avoiding growing only one sub-array 
    i.e. to avoid if too many keys, mapping to same index i.e. same array due to 
    fixed length self.size parameter
    '''
    def _resize(self):
        new_size = self.size * 2  # Double the size
        new_buckets = [[] for _ in range(new_size)]
        # Rehash all elements into new buckets
        for key, value in enumerate(self.buckets):
            new_index = key % new_size
            for i, (k, v) in enumerate(self.buckets[new_index]):
                print(f"Info i, k, and v: {i} and {k} and {v}")
                new_buckets[new_index].append((k, v))
        self.size = new_size
        self.buckets = new_buckets

    # _hash function to get the index of the bucket
    def _hash(self, key):
        return key % self.size
    
    # put function to add key-value pair to the hashmap
    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        print(f"Info put-bucket_index: {bucket_index}")
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            print(f"Info i, k, and v: {i} and {k} and {v}")
            '''overwrite new value in hashmap if key already exist'''
            if k == key:
                self.buckets[bucket_index][i] = (key, value)
                return           
        '''add new key-value in hashmap'''
        self.buckets[bucket_index].append((key, value))
        self.num_elements += 1  # Increment element count
        # Check load factor and resize if needed
        if self.num_elements / self.size > self.load_factor_threshold:
            print(f"Time to resize-1")
            self._resize()

    # delete function to remove the key-value pair from the hashmap
    def delete(self, key: int) -> None:
        bucket_index = self._hash(key)
        # print(f"Info delete-buckets: {self.buckets}")
        print(f"Info delete-bucket_index: {bucket_index}")
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            print(f"Info i, k, and v: {i} and {k} and {v}")
            if k == key:
                # self.buckets[bucket_index].remove((k, v))
                del self.buckets[bucket_index][i]
                self.num_elements -= 1

    # get function to get the value of the key from the hashmap
    def get(self, key: int) -> bool:
        bucket_index = self._hash(key)
        print(f"Info get-bucket_index: {bucket_index}")
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            print(f"Info i, k, and v: {i} and {k} and {v}")
            if k == key:
                return v
        return -1
        
myHashMap = MyHashMap()
# myHashMap.put(2, 30000)
# print(vars(myHashMap))
# myHashMap.put(20, 30000)
# print(vars(myHashMap))
# myHashMap.put(1987, 30033)
# print(vars(myHashMap))
# myHashMap.put(12, 400000)
# print(vars(myHashMap))
# myHashMap.put(2, 566000)
# print(vars(myHashMap))
# result = myHashMap.get(1987)
# print(result)
# myHashMap.delete(1987)
# print(vars(myHashMap))
# result = myHashMap.get(1987)
# print(result)

myHashMap.put(1, 1); # The map is now [[1,1]]
myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
print(myHashMap.buckets)
result1 = myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
print(result1)
result2 = myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(result2)
myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.buckets)
result3 = myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
print(result3)
myHashMap.delete(2); # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.buckets)
result4 = myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]
print(result4)