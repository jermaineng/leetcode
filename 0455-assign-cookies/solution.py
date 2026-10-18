class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            
            j += 1 # need larger cookie

        return count 

# greedy
# look at child with least greed and try to assign smallest cookie
