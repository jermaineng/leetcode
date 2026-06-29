class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        count = {}
        left = 0

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)

            while count[c] > 1:
                count[s[left]] -=1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
