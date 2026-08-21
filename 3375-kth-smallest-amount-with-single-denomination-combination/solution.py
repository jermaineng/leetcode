class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
    
        base_coins = []
        for x in coins:
            if all(x % c for c in base_coins):
                base_coins.append(x)
    
        def check(m):
            tot = 0
            for x in range(1, len(base_coins) + 1):
                for c in combinations(base_coins, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * base_coins[0] + 1), True, lo=1, key=check)
