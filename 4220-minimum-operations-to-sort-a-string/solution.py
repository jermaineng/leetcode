class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0
        
        if n == 2: # unsorted and length 2
            return -1 
        
        if s[0] == min(s) or s[-1] == max(s):
            return 1
        
        if min(s) in s[:-1] or max(s) in s[1:]:
            return 2

        return 3


# possible cases: 0
# 1: first/ last letter is alrdy sorted
# -1: length 2 unsorted
# 2: min is before last or max is after first
# 3: min stuck at last and max stuck at first
