class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # defaultdict automatically creates an empty list for a key if it doesnt exist in the dict

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            ans[tuple(count)].append(s)
        
        return list(ans.values())
