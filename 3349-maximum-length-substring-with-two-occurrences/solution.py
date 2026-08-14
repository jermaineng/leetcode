class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0] * 26

        ans = 0
        left = 0

        for right, c in enumerate(s):
            idx = ord(c) - ord('a')
            freq[idx] += 1

            while freq[idx] > 2:
                left_idx = ord(s[left]) - ord('a')
                freq[left_idx] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans 

# array of size 26 to keep track of freq for each letter
# sliding window and record max length
# extend window if at most two occurrences
# otherwise shrink window
