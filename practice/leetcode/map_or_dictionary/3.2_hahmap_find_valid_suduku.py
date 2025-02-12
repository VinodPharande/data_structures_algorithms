"""
Valid Sudoku

Solution
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        if key not in self.data:
            self.data[key] = set()
        if value in self.data[key]:  # If value already exists, return False (invalid board)
            return False
        self.data[key].add(value)
        return True
    
    '''using custom hashmap or dictionary'''
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = Solution()
        cols = Solution()
        boxes = Solution()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                box_index = (r // 3, c // 3)

                if not rows.add(r, num) or not cols.add(c, num) or not boxes.add(box_index, num):
                    return False

        return True
    
    '''using built-in hashset'''
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
    #     rows = [set() for _ in range(9)]
    #     cols = [set() for _ in range(9)]
    #     boxes = [set() for _ in range(9)]
        
    #     for r in range(9):
    #         for c in range(9):
    #             num = board[r][c]
    #             if num == '.':
    #                 continue
                
    #             box_index = (r // 3) * 3 + (c // 3)
                
    #             if num in rows[r] or num in cols[c] or num in boxes[box_index]:
    #                 return False
                
    #             rows[r].add(num)
    #             cols[c].add(num)
    #             boxes[box_index].add(num)
        
    #     return True

    '''using built-in hashmap'''
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
    #     from collections import defaultdict
    #     rows = defaultdict(set)
    #     cols = defaultdict(set)
    #     boxes = defaultdict(set)
        
    #     for r in range(9):
    #         for c in range(9):
    #             num = board[r][c]
    #             if num == '.':
    #                 continue
                
    #             box_index = (r // 3, c // 3)
                
    #             if num in rows[r] or num in cols[c] or num in boxes[box_index]:
    #                 return False
                
    #             rows[r].add(num)
    #             cols[c].add(num)
    #             boxes[box_index].add(num)
        
    #     return True



# Example usage:
obj = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]   
print(f"Board: {board}")
print(obj.isValidSudoku(board))  # True
