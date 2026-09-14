class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x1, y1, x2, y2
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

# when x doesnt overlap: x2 > x1 of other rect
# when y doesnt overlap: y2 > y1 of other rect

# x1, y2      x2, y2
# x1, y1      x2, y1
