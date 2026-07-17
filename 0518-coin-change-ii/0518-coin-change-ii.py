from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        
        def f(i, t):
            # Base Case: If we are at the first coin
            if i == 0:
                # If the remaining amount is divisible by this coin, there is exactly 1 way to make it.
                if t % coins[i] == 0:
                    return 1
                else:
                    # Otherwise, there are 0 ways.
                    return 0
            
            # Return memoized result if already computed
            if dp[i][t] != -1:
                return dp[i][t]
            
            # Option 1: Don't take the current coin
            nontake = f(i - 1, t)
            
            # Option 2: Take the current coin (if it doesn't exceed the target)
            take = 0
            if coins[i] <= t:  # Note: Changed from `<` to `<=`
                take = f(i, t - coins[i]) # Note: We don't add 1 here because we are counting combinations, not coins
                
            # Total combinations is the sum of both choices
            dp[i][t] = take + nontake
            return dp[i][t]
            
        # Start the recursion from the last index and the total amount
        return f(n - 1, amount)