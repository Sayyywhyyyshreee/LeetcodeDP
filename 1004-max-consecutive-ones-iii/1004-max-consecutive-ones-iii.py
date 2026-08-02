class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxi=0
        zero=0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
            while zero > k:
            
                if nums[l] == 0:
                    zero -= 1
                l += 1
            maxi = max(maxi,r-l+1)
        return maxi

        