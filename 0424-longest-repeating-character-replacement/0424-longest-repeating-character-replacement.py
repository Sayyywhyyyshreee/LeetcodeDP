class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxf=0
        maxl=0
        mpp={}
        for r in range(len(s)):
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                 mpp[s[r]] = 1
            maxf = max(maxf, mpp[s[r]])
            while (r-l+1) - maxf > k:
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    del mpp[s[l]]
                l+= 1
            maxl = max(maxl, r-l+1)
        return maxl



        