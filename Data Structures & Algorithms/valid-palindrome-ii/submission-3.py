class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                sL = s[l+1:r+1]
                sR = s[l:r]
                return sL == sL[::-1] or sR == sR[::-1]
            l, r = l+1, r-1
        return True