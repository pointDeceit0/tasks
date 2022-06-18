class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(list(set(nums))) != len(nums) else False
        

a = Solution()

print(a.containsDuplicate([1,2,3,1]))
print(a.containsDuplicate([1,2,3,4]))
print(a.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))