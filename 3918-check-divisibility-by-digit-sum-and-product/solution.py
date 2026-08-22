class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_digits = 0
        product_digits = 1
        curr = n

        while curr > 0:
            digit = curr % 10
            sum_digits += digit
            product_digits *= digit
            curr //= 10
        
        return n % (sum_digits + product_digits) == 0
