class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n
        
        count = i = 0

        while i <= n - k:
            if s[i:i + k] == s[i:i + k][::-1]:
                i += k
                count += 1
            
            elif i + k + 1 <= n and s[i:i + k + 1] == s[i:i + k + 1][::-1]:
                i += k + 1
                count += 1
            
            else:
                i += 1
        
        return count

# we want palindrome length to be as small as possible so
# palindrome length is either k or k + 1
