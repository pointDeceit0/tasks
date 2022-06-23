class List(list):
    ...


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            time  O(n)
            space O(1)
        
        """
        cur_num = 0
        max_num = nums[0]
        for num in nums:
            if cur_num < 0: cur_num = 0
                
            cur_num += num
            max_num = max(max_num, cur_num)
            
        return max_num


a = Solution()

print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([1]))
print(a.maxSubArray([5,4,-1,7,8]))
        