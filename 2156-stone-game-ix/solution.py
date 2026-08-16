class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remainder_count = [0, 0, 0]

        for stone in stones:
            remainder_count[stone % 3] += 1

        if remainder_count[0] % 2 == 0:
            return min(remainder_count[1], remainder_count[2]) >= 1

        return abs(remainder_count[1] - remainder_count[2]) >= 3
