class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n)]
        def f(ind,t):
            
           
            if ind == 0:
                if t % coins[0] == 0:
                    return t//coins[0]
                else:
                    return float('inf')
            if dp[ind][t] != -1:
                return dp[ind][t]
            nontake = 0 + f(ind-1,t)
            take = float('inf')
            if coins[ind] <= t:
                take = 1 + f(ind,t-coins[ind])
            dp[ind][t] = min(take,nontake)
            return dp[ind][t] 
        ans = f(n - 1, amount)
        return ans if ans != float('inf') else -1
            

        