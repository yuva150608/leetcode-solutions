class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        
        res = []
        # Check sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        num, den = abs(numerator), abs(denominator)
        
        # Integer part
        res.append(str(num // den))
        num %= den
        
        if num == 0:
            return "".join(res)
            
        # Fractional part
        res.append(".")
        remainders = {}
        
        while num != 0:
            if num in remainders:
                res.insert(remainders[num], "(")
                res.append(")")
                break
            
            remainders[num] = len(res)
            num *= 10
            res.append(str(num // den))
            num %= den
            
        return "".join(res)
