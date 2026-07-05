class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # Equal partition is impossible if total sum is odd
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        # dp[i][t] = Can we make sum 't' using elements from index 0 to i?
        dp = [[False] * (target + 1) for _ in range(n)]

        # Base case: Sum 0 is always possible
        for i in range(n):
            dp[i][0] = True

        # Base case: Using only the first element
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # Fill the table from top to bottom
        for i in range(1, n):
            for t in range(1, target + 1):

                # Don't take current element
                notTake = dp[i - 1][t]

                # Take current element
                take = False
                if nums[i] <= t:
                    take = dp[i - 1][t - nums[i]]

                dp[i][t] = take or notTake

        # Whole array = indices 0...n-1
        return dp[n - 1][target]