from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # 1. Convert to Partition Equal Subset Sum problem
        # If (total + target) is odd or target is out of bounds, it's impossible
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
            
        s1 = (total + target) // 2
        n = len(nums)
        
        # 2. Setup the "prev" array to count ways (integers instead of booleans)
        prev = [0] * (s1 + 1)
        
        # Base case for the first element (nums[0])
        # If the first element is 0, there are 2 ways to make sum 0 (take it or don't take it)
        if nums[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1  # 1 way to make sum 0 (don't take it)
            if nums[0] <= s1:
                prev[nums[0]] = 1  # 1 way to make sum nums[0] (take it)

        # 3. DP Transitions
        for i in range(1, n):
            curr = [0] * (s1 + 1)
            
            # Start t from 0 because taking a '0' from nums changes the count of ways
            for t in range(s1 + 1): 
                notTake = prev[t]
                
                take = 0
                if nums[i] <= t:
                    take = prev[t - nums[i]]
                
                # Instead of "or", we add the ways together
                curr[t] = take + notTake
                
            prev = curr

        return prev[s1]