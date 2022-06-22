class List(list):
    ...

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return nums

        ''' time complexity  == O(n)
            space complexity == O(n) '''

        ''' I N I T I A L I Z A T I O N '''
        rev, ans = nums[::-1], [1]
        prefix, postfix = nums[0], rev[0]
        n = len(nums)

        ''' S O L U T I O N '''
        for i in range(n - 2):
            ans.append(prefix)
            prefix *= nums[i + 1]
            
        for i in range(n - 2, -1, -1):
            ans[i] *= postfix
            postfix *= rev[n - i - 1]

        ans.append(prefix)
        return ans 


a = Solution()

print(a.productExceptSelf([]))
print(a.productExceptSelf([0])) # about this solution --- LeetCode accepts these
print(a.productExceptSelf([6]))
print(a.productExceptSelf([6, 9]))
print(a.productExceptSelf([6, 9, 10]))
print(a.productExceptSelf([1, 2, 3, 4, 5, 6, 7]))
print(a.productExceptSelf([-1,1,0,-3,3]))
print(a.productExceptSelf([1,2,3,4]))
        