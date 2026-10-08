class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0 # nesting bracs
        ans = ""

        for brac in s:
            if brac == "(":
                if depth > 0:
                    ans += brac
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans += brac
        
        return ans

