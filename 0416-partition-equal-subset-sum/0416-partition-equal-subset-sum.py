class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n)]

        # Sum 0 is always possible
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        

        # Fill table backwards
        for i in range(1,n):
            for t in range(1, target + 1):

                notTake = dp[i - 1][t]

                take = False
                if nums[i] <= t:
                    take = dp[i - 1][t - nums[i]]

                dp[i][t] = take or notTake

        return dp[n-1][target]