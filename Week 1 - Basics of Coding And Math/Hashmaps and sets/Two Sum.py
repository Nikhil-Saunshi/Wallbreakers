class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in d:
                return d[find], i
            d[nums[i]] = i