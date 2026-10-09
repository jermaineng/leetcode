class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        ins = 0 # number of insertions
        open_count = 0 # open brackets that dont have "))"

        i = 0
        while i < n:
            if s[i] == "(":
                open_count += 1
            else:
                if i + 1 < n and s[i + 1] == ")":
                    i += 1
                else:
                    ins += 1 # insert ")"

                # check whether can match open bracs with curr "))"
                if open_count > 0:
                    open_count -= 1
                else:
                    ins += 1 # if not insert an open brac
            
            i += 1

        ins += open_count * 2
        return ins
