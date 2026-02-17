class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_n, closed_n, path):
            # Base case: we've used n pairs
            if open_n == closed_n == n:
                res.append(path)
                return
            
            # Rule 1: We can add an opening bracket if we have some left
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
            
            # Rule 2: We can only add a closing bracket if it balances an open one
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
        
        backtrack(0, 0, "")
        return res
