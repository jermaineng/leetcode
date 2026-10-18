class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}

        i = 0
        end = 0
        length = 1
        parts = []

        while i < len(s):
            end = max(end, last[s[i]])

            if i == end:
                parts.append(length)
                length = 0

            i += 1
            length += 1

        return parts

# greedy: track last occurrence of each letter then
# check curr partition pos with max of last occurrence
