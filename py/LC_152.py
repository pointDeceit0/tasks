class Solution(object):
    def maxProduct(self, nums):
        min_val, max_val, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):

            max_val, min_val = max(nums[i], max_val * nums[i], min_val * nums[i]), min(nums[i], min_val * nums[i], max_val * nums[i])
            ans = max(ans, max_val)

        return ans 


def test():
    s = Solution()

    assert s.maxProduct([-1, -2, -3]) == 6 
    assert s.maxProduct([-2,0,-1]) == 0 
    assert s.maxProduct([2,3,-2,4]) == 6
    assert s.maxProduct([2, -3, 4, -2, 3, -1, 2]) == 144
    assert s.maxProduct([2, -3, 4, -2, 3, -1, 2, -1]) == 288
    assert s.maxProduct([2, -3, 4, -2, 0, 3, -1, 2, -1]) == 48
    assert s.maxProduct([2,-5,-2,-4,3]) == 24
    #assert s.maxProduct() == 


def main():
    test()


if __name__ == "__main__":
    main()