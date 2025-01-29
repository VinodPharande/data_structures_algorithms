'''
Design HashSet

Solution
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 10**6
At most 10**4 calls will be made to add, remove, and contains.
'''

''' Implementation using python "list" collection which is a dynamic array '''
class MyHashSet:

    def __init__(self):
        self.size = 10
        self.buckets = [ [] for _ in range(self.size)]

    def _hash(self, key) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if 0 <= key <= 10**6:
            bucket_index = self._hash(key)
            if key not in self.buckets[bucket_index]:
                self.buckets[bucket_index].append(key)

    def remove(self, key: int) -> None:
        if 0 <= key <= 10**6:
            bucket_index = self._hash(key)
            if key in self.buckets[bucket_index]:
                self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        if 0 <= key <= 10**6:
            bucket_index = self._hash(key)
            return key in self.buckets[bucket_index]
        return False

''' Example Usage '''
myHashSet = MyHashSet()
myHashSet.add(1);      # set = [1]
print(myHashSet.buckets)
myHashSet.add(2);      # set = [1, 2]
print(myHashSet.buckets)
result1 = myHashSet.contains(1); # return True
print(f"{myHashSet.buckets} and {result1}")
result2 = myHashSet.contains(3); # return False, (not found)
print(f"{myHashSet.buckets} and {result2}")
myHashSet.add(2);      # set = [1, 2]
print(myHashSet.buckets)
result3 = myHashSet.contains(2); # return True
print(f"{myHashSet.buckets} and {result3}")
myHashSet.remove(2);   # set = [1]
result4 = myHashSet.contains(2); # return False, (already removed)
print(f"{myHashSet.buckets} and {result4}")



''' [Not Complete]: Implementation using python "Set" collection or data structure'''        
class MyHashSetUsingSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hashset