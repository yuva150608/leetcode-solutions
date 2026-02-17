class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            tmp = ""
            i = 0
            while i < len(res):
                count = 1
                # Group consecutive identical digits
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                # Append count then the digit
                tmp += str(count) + res[i]
                i += 1
            res = tmp
        return res
