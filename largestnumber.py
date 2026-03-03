from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Convert integers to strings
        strs = [str(num) for num in nums]
        
        # Custom comparator: compare a+b with b+a
        def compare(a, b):
            if a + b > b + a:
                return -1  # a comes first
            else:
                return 1   # b comes first
        
        # Sort using the custom comparator
        strs.sort(key=cmp_to_key(compare))
        
        # Join strings together
        result = "".join(strs)
        
        # Edge case: if the largest number is "0" (e.g., input [0, 0])
        return "0" if result[0] == "0" else result
