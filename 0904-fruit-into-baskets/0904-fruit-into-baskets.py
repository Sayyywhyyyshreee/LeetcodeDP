class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        maxi=0
        mpp = {}
        for r in range(len(fruits)):
            if fruits[r] in mpp:
                mpp[fruits[r]] += 1
            else:
                mpp[fruits[r]] = 1
            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0: 
                    del mpp[fruits[l]]
                l += 1
            maxi = max(maxi,r-l+1)
        return maxi

        