class List(list):
    pass

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Binary solution
        # Numbers mutually destroy each other and only the answer remains
        # because: 3^3=0, 7^7=0
        n = 0

        for i in nums: n ^= i
        for i in range(len(nums)): n ^= i

        return n^(i + 1)

        '''return sum(range(len(nums) + 1)) - sum(nums)'''

        '''
        Obvious solution
        Time  --- O(nlogn)
        Space --- O(1)

        nums.sort()
    
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums) - 1'''

    
s = Solution()

assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8