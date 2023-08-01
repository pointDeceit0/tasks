class Solution(object):
    def productExceptSelf(self, nums):

        # quite effective, but not a very nice code
        count = 0
        product = 1

        for v in nums:
            if v == 0:
                count += 1
            else:
                product *= v
        
        if count > 1:
            return [0] * len(nums)
        
        ans = []

        if count == 1:
            for v in nums:
                if v == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            return ans
        
        # else
        for v in nums:
            ans.append(product // v)
        return ans