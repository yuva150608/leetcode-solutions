class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Result array for max possible length
        res = [0] * (len(num1) + len(num2))
        
        # Multiply each digit pair from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Product of two digits
                prod = int(num1[i]) * int(num2[j])
                # Add to the appropriate positions in res array
                res[i + j + 1] += prod
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] %= 10
        
        # Convert to string, skipping leading zero if it exists
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:]))
