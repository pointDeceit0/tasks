class List(list):
    pass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        """
        time complexity  --- O(log n)
        space complexity --- O(1)
        
        """
        while l != r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1

            elif nums[m] < nums[r]:
                r = m

        ans = self.binary_search(nums[l:], target) + l
        ans = self.binary_search(nums[:l], target) if ans - l == -1 else ans 
        
        return ans 

    def binary_search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1

        l, r = 0, len(nums)
        while l != r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                r = m

            elif nums[m] < target:
                l = m + 1
        
        return -1

a = Solution()

print(a.search([1], 1))
print(a.search([4,5,6,7,0,1,2], 0))
print(a.search([1], 0))
print(a.search([1,2,3,4,5,6,7,8,9] , 3))
print(a.search([4,5,6,7,0,1,2], 3))