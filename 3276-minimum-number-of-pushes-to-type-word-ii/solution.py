class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        n = len(word)
        for c in word:
            freq[ord(c) - ord('a')] += 1
        
        freq.sort(reverse=True) # sorts in descending order

        ans = 0
        for i, f in enumerate(freq):
            ans += f * (i // 8 + 1)
        
        return ans
    
    # array of size 26 to count freq of each character
    # sort freq
    # number of pushes = freq * (i // 8 + 1)
