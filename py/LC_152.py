class List(list):
    pass

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        s = max(nums)  
        m = M = 1
        for num in nums:
            if num == 0:
                M = m = 1

            cur_max = M * num
            M = max(cur_max, num * m, num)
            m = min(cur_max, num * m, num)

            s = max(s, M, m)

        return s 


a = Solution()

print(a.maxProduct([2,3,-2,4]))
print(a.maxProduct([-1, -1]))
print(a.maxProduct([2,3,-2, 4, -3, 0, 6, 20]))
print(a.maxProduct([-2,0,-1]))
print(a.maxProduct([2]))
print(a.maxProduct([2,-5,-2,-4,3]))
print(a.maxProduct([3,-2,-10,-8,4]))