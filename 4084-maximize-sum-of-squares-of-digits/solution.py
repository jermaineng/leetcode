class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = ""

        while num > 0:
            if sum < 10:
                curr = sum
            else:
                curr = 9
            
            ans += str(curr)
            sum -= curr
            num -= 1
        
        return ans

# if the sum < 10, start with sum as first digit
# else, start with 9
# subtract digit chosen from sum
# repeat until length of number matches num
