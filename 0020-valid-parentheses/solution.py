class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        brac = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in brac.values():
                stack.append(c)
            
            elif c in brac:
                if not stack or stack.pop() != brac[c]:
                    return False

        return not stack # if stack is not empty (still has unmatched bracs)
