class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        
        def backtrack(index, path, current_val, prev_val):
            # Base Case: Reached the end of the string
            if index == len(num):
                if current_val == target:
                    res.append(path)
                return

            for j in range(index, len(num)):
                # Avoid leading zeros (e.g., "05" is invalid, but "0" is fine)
                if j > index and num[index] == '0':
                    break
                
                # Get the current substring and convert to int
                sub_str = num[index:j+1]
                val = int(sub_str)
                
                if index == 0:
                    # First number, no operator needed
                    backtrack(j + 1, sub_str, val, val)
                else:
                    # Try Addition
                    backtrack(j + 1, path + "+" + sub_str, current_val + val, val)
                    
                    # Try Subtraction
                    backtrack(j + 1, path + "-" + sub_str, current_val - val, -val)
                    
                    # Try Multiplication:
                    # To respect precedence, we "undo" the previous value and then multiply
                    # New val = (current_val - prev_val) + (prev_val * val)
                    backtrack(j + 1, path + "*" + sub_str, 
                              (current_val - prev_val) + (prev_val * val), 
                              prev_val * val)

        backtrack(0, "", 0, 0)
        return res
