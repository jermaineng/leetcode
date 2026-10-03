class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0

        for i, b in enumerate(s):
            if b == '(':
                stack.append(i)

            else:
                stack.pop()
            
                if len(stack) == 0:
                    # curr index is new invalid index
                    stack.append(i)
                else: 
                    # stack only contains index of most recent invalid index
                    # substring length is i - that index
                    count = max(count, i - stack[-1])

        return count

# stack which keeps track of most recent invalid index and then single '(' indexes
# push when open, pop when close

