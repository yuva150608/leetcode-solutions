class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def compute(expr):
            # Return cached result if already calculated
            if expr in memo:
                return memo[expr]
            
            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Divide: Solve left and right parts recursively
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    # Conquer: Combine results based on current operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            # Base case: If no operators, the expression is just a number
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res

        return compute(expression)
