class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set()
        m = 0
        l = 0
        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l+=1
            t.add(s[r])
            m = max(m, r-l+1)
            
        return m