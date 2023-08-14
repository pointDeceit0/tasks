class Solution(object):
    def maxSubArray(self, nums):
        """
        It turns out that algorithm I wrote is called Kadane's algorithm 
        """
        ans, prev = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            prev = max(nums[i], nums[i] + prev)
            ans = max(prev, ans)

        return ans



        '''
        [-2,1,-3,4,-1,2,1,-5,4]
        [4,-1,2,1]
        '''


def test():
    s = Solution()

    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.maxSubArray([5,4,-1,7,8]) == 23
    assert s.maxSubArray([1]) == 1


def main():
    test()


if __name__ == "__main__":
    main()