class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        prev = [False] * (target + 1) 
        # Sum 0 is always possible
        prev[0] = True
        if nums[0] <= target:
            prev[nums[0]] = True

        

        
        for i in range(1,n):
            curr = [False] * (target + 1) 
            curr[0] = True
            for t in range(1, target + 1):

                notTake = prev[t]

                take = False
                if nums[i] <= t:
                    take = prev[t - nums[i]]

                curr[t] = take or notTake
            prev = curr

        return prev[target]