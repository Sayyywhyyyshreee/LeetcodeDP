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

        # Base case: last index
        if nums[n - 1] <= target:
            dp[n - 1][nums[n - 1]] = True

        # Fill table backwards
        for i in range(n - 2, -1, -1):
            for t in range(1, target + 1):

                notTake = dp[i + 1][t]

                take = False
                if nums[i] <= t:
                    take = dp[i + 1][t - nums[i]]

                dp[i][t] = take or notTake

        return dp[0][target]