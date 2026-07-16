class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n)]
       
            
        for t in range(0,amount+1):
                if t % coins[0] == 0:
                    dp[0][t] = t//coins[0]
                else:
                    dp[0][t] = float('inf')
        for i in range(1,n):
            for t in range(0,amount+1):
                nontake = 0 + dp[i-1][t]
                take = float('inf')
                if coins[i] <= t:
                    take = 1 + dp[i][t-coins[i]]
                dp[i][t] = min(take,nontake)
                
        ans = dp[n - 1] [amount]
        return ans if ans != float('inf') else -1
            

        