class Solution:
    def reverseDegree(self, s: str) -> int:
        deg = 0
        n = len(s)

        for i in range(n):
            rev_idx = ord('z') - ord(s[i]) + 1
            deg += rev_idx * (i + 1)
        
        return deg

