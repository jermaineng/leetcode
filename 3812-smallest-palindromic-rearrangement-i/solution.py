class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 3:
            return s
        
        half = s[:n // 2]
        count = Counter(half)

        left = []
        for c in sorted(count):
            left.append(c * count[c])

        left = "".join(left) # appends the list of strings in left
        mid = s[n // 2] if n % 2 else ""

        return left + mid + left[::-1]

# get freq count of letters for half the string
# iterate through array of counts and construct half
# if odd length string, keep middle character
# append reverse of that half
