class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 1: return [0]
        
        hash = dict()
        
        for i in range(len(nums)):
            delta = target - nums[i]
            
            if delta in hash:
                return [hash[delta], i]
            
            hash[nums[i]] = i
            
        return -1
