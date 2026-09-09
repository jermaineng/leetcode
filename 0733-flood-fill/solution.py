class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori = image[sr][sc]
        if ori == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if image[r][c] != ori:
                return
            
            image[r][c] = color

            dfs(r - 1, c) # down
            dfs(r + 1, c) # up
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        dfs(sr, sc)
        return image
