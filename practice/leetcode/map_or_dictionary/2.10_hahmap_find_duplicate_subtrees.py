"""
Find Duplicate Subtrees

Solution
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
 

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:
The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""

'''using bulit-in dictionary'''
# from collections import defaultdict
# from typing import Optional, List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[TreeNode]:
#         subtree_map = defaultdict(int)  # Stores frequency of subtree serialization
#         result = []
#         seen = set()  # To track already added duplicate roots

#         '''The serialize(node) function is called inside itself because it follows a recursive approach 
#         to perform a postorder traversal (left → right → root) of the tree.

#         Why Is serialize(node) Called Inside the Function?
#         Each call to serialize(node):

#         Processes the left subtree → serialize(node.left)
#         Processes the right subtree → serialize(node.right)
#         Constructs a unique string representation of the subtree using node.val, left_serial, and right_serial.
#         Step-by-Step Execution
#         Consider this tree:

#         plaintext
#         Copy
#         Edit
#                 1
#             / \
#             2   3
#             /   / \
#             4   2   4
#             /
#             4
#         The recursive function works like this:

#         Start at root (1) → Calls serialize(2) and serialize(3).
#         Process left subtree (2):
#         Calls serialize(4).
#         serialize(4) returns "4,#,#", as it has no children.
#         Subtree "2,4,#,#,#" is created.
#         Process right subtree (3):
#         Calls serialize(2), which calls serialize(4).
#         Calls serialize(4), returns "4,#,#".
#         Subtree "2,4,#,#,#" is created again.
#         Calls serialize(4), returns "4,#,#".
#         Subtree "3,2,4,#,#,#,4,#,#" is created.
#         Final serialization for root (1):
#         "1,2,4,#,#,#,3,2,4,#,#,#,4,#,#"
#         Since "4,#,#" appears multiple times, the function detects 4 as a duplicate.

#         Why Can't We Avoid Calling serialize() Inside Itself?
#         Recursion is necessary to traverse and process each node’s left and right subtrees before handling the root.
#         Each call computes a unique signature, ensuring that we correctly identify duplicate subtrees.
#         Without recursion, we would have to use an explicit stack or queue, making the implementation more complex.
#         Key Takeaway
#         The recursive function ensures: 
#         ✅ Each node's subtree is uniquely serialized
#         ✅ Duplicate subtrees are identified correctly
#         ✅ Postorder traversal is maintained (left → right → root)
#         '''
#         def serialize(node):
#             if not node:
#                 return "#"

#             left_serial = serialize(node.left)
#             right_serial = serialize(node.right)

#             # Create a unique string representation of the subtree
#             subtree_serial = f"{node.val},{left_serial},{right_serial}"

#             # Check if this subtree has appeared twice
#             if subtree_map[subtree_serial] == 1:  
#                 result.append(node)  # Add root of duplicate subtree

#             subtree_map[subtree_serial] += 1
#             return subtree_serial

#         serialize(root)
#         return result


# # Example Tree Construction
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(4)
# root.right.left.left = TreeNode(4)

# # root = [1,2,3,4,None,2,4,None,None,4]
# # Run the function
# solution = Solution()
# duplicates = solution.findDuplicateSubtrees(root)
# print(list(map(lambda x: x.val, duplicates)))
# # Print output
# # for node in duplicates:
# #     print(node.val)


'''
 What Is Serialization of a Subtree?
Serialization of a subtree means converting the structure and values of a subtree into a string format. 
This helps in uniquely identifying and comparing subtrees.
'''


'''using custom dictionary'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[TreeNode]:
        subtree_map = {}  # Using a regular dictionary instead of defaultdict
        result = []

        def serialize(node):
            if not node:
                return "#"

            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            subtree_serial = f"{node.val},{left_serial},{right_serial}"

            # Check if the serialized subtree exists in the dictionary
            if subtree_serial in subtree_map:
                subtree_map[subtree_serial] += 1
            else:
                subtree_map[subtree_serial] = 1

            # Add to result only when encountered the second time
            if subtree_map[subtree_serial] == 2:
                result.append(node)

            return subtree_serial

        serialize(root)
        return result

# Manually constructing the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
# Run the function
solution = Solution()
duplicates = solution.findDuplicateSubtrees(root)
print(list(map(lambda x: x.val, duplicates)))
# Print output
# for node in duplicates:
#     print(node.val)
