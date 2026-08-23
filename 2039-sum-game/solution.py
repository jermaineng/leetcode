class Solution:
    def sumGame(self, num: str) -> bool:
        s, q = [0, 0], [0, 0]
        n = len(num)

        for i in range(n):
            j = i // (n // 2)
            if num[i] == '?':
                q[j] += 1
            else:
                s[j] += int(num[i])

        return (q[0] + q[1]) & 1 == 1 or (s[0] - s[1]) != (q[1] - q[0]) * 4.5
