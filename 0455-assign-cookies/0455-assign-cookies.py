class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g is None or s is None:
            return 0
        childr=0
        maxi=0
        g.sort()
        s.sort()
        l=0
        r=0
        n= len(g)
        m = len(s)
        while r < n and l < m:
            if s[l] >= g[r]:
                childr += 1
                l+=1
                r+=1
                maxi= max(childr, maxi)
            else:
                l+=1
        return maxi
        