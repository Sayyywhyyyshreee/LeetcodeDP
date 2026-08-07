class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf=0
        maxl=0
        mpp = {}
        for r in range(len(s)):
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            maxf = max(maxf, mpp[s[r]])
            if r-l+1 - maxf > k:
                mpp[s[l]] -= 1
                l += 1
            maxl = max(maxl,r-l+1)
        return maxl
        