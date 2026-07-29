class Solution:
    # ways to choose r positions out of n positions
    def comb(self, n, r, k):
        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i
            if ans >= k:
                return k # stops early because we just need to know whether its at least k

        return ans
    
    # counts distinct permutations of the remaining char by choosing positions for each character frequency
    def count_permut(self, count, k):
        total = sum(count)
        ans = 1

        for f in count:
            if f:
                ans *= comb(total, f)
                if ans >= k:
                    return k
                total -= f

        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = [0] * 26
        n = len(s)
        m = n // 2

        for c in s[:m]:
            count[ord(c) - ord('a')] += 1

        if self.count_permut(count, k) < k:
            return ""

        half = []

        for _ in range(m):
            for i in range(26):
                if count[i] == 0:
                    continue
                
                count[i] -= 1 # take this char as possible first char

                ways = self.count_permut(count, k)

                if k > ways:
                    k -= ways
                    count[i] += 1
                else:
                    half.append(chr(i + ord('a')))
                    break
        
        left = "".join(half)
        mid = s[m] if n % 2 else ""

        return left + mid + left[::-1]
        
# array of size 26 to store freq of characters in half of the string
# while constructing half:
# for every char from a to z, if the character exists, "use" it as first char and count possible permutations for remaining freq
# if count >= k, use this char
# otherwise next char and update back freq

# NOTE: we only need to know whether this count reaches k, because any value larger than k means this group already contains the k-th permutation
