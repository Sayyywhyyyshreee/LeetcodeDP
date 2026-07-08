class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for index, value in enumerate(nums):
            rem = target - value
            if rem in maps:
                return (maps[rem],index)
            maps[value] = index
        return
        