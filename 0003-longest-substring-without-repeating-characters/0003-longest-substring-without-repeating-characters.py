class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp= set()
        maxlen=0
        l=0
        for r in range(len(s)):
            while s[r] in mpp:
                mpp.remove(s[l])
                l+=1
            mpp.add(s[r])
            maxlen= max(maxlen,r-l+1)
        return maxlen
        
        