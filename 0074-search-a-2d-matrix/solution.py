class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            # convert flattened index back to row or col
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# treat the matrix as a 1D sorted array because each row starts after the previous row ends
# perform binary search
# convert the 1D index back to row and column using division and modulo

# above is more optimised
# perform binary search on the first col to find out which row target is in because each int in first col is larger than last int of prev row
# then perform binary search on the row to find target

# def searchMatrix:
#     rows, cols = len(matrix), len(matrix[0])

#     # Find the row containing target
#     top, bottom = 0, rows - 1

#     while top <= bottom:
#         row = (top + bottom) // 2

#         if target < matrix[row][0]:
#             bottom = row - 1
#         elif target > matrix[row][-1]:
#             top = row + 1
#         else:
#             break
#     else:
#         return False

#     # Binary search within the row
#     left, right = 0, cols - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if matrix[row][mid] == target:
#             return True
#         elif matrix[row][mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return False
