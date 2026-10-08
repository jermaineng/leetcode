class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)

        left = 0
        for i in range(n - 1, -1, -1):
            if colors[0] != colors[i]:
                left = i
                break

        right = 0
        for i in range(n):
            if colors[n - 1] != colors[i]:
                right = n - 1 - i
                break
        
        return max(left, right)

# want smallest possible index for left house and largest possible for right
# start at ends
