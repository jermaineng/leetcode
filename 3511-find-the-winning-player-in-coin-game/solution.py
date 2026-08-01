class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        rounds = min(x, y >> 2)

        return "Alice" if rounds % 2 != 0 else "Bob" 
