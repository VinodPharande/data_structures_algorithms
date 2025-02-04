'''
Happy Number

Solution
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # seen.clear()
        if 1 <= n <= 231 - 1:
            while n != 1 and n not in seen:
                new_n = 0  # Initialize sum of squares
                seen.add(n)
                print(f"Info seen-2: {seen}")
                '''using list compreension'''
                # n = sum(int(i) ** 2 for i in str(n))
                '''using normal for loop'''
                for i in str(n):
                    print(f"for {i}: {i}")
                    new_n += int(i) ** 2
                    print(f"for new_n-{i}: {new_n}") 
                n = new_n  # Update n with the sum of squares
                print(f"Info n: {n}")
                print(f"********************************")
            return n == 1
        else:
            print("ValueError: n must be between 1 and 231 - 1")
            raise ValueError("Array lengths must be between 1 and 1000")
        
        
n = 19  # True
# n = 12  # False
# n = 345  # raise Exception
solution = Solution()
result = solution.isHappy(n)
print(result)  # Output: True
print("Happy Number")  # Output: Happy Number
        