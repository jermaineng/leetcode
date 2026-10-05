class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # memo = {}
        # n = len(s)
        # def f(i):
        #     if i < 0: 
        #         return 0
        #     if i == 0:
        #         return 1
        #     if i in memo:
        #         return memo[i]
        #     val = 0
        #     if s[i-1] != '0':
        #         val += f(i-1)
        #     if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
        #         val += f(i-2)
                
        #     memo[i] = val
        #     return val
            
        # return f(n)
        
        
        # dp[i] counts curr valid decodes for first i
        # index i can be by itself or appended to i - 1 if <= 26
        # if s[i - 1] is 1 - 9 then can add dp[i - 1]
        # if s[i - 2 : i] <= 26 then can add dp[i - 2] 
        # dp[i] = dp[i - 1] + dp[i - 2]
        
        # dp[1] = 1 if s[1] != 0, dp[1] == 0 if s[1] == 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        
        for i in range(2, n + 1):
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]  
