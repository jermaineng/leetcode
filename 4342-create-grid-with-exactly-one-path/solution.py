class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if n == 1:
            return ['.' for _ in range(m)]
        
        grid = [['#'] * n for _ in range(m)]

        # move right by 1 step
        grid[0][0] = '.'
        grid[0][1] = '.'

        # move alll the way down
        for i in range(1, m):
            grid[i][1] = '.'
        
        # move all the way right
        for i in range(2, n):
            grid[m - 1][i] = '.'
        
        return [''.join(row) for row in grid]
