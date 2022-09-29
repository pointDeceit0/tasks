class List(list):
    pass


class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' Top -> down solution
        time  --- O(n)
        space --- O(n)
        '''

        dp = [0] * (len(nums) + 3)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], nums[i] + dp[i + 3], nums[i])

        return max(dp)


def test():
    a = Solution()

    assert a.rob([1,2,3,1]) == 4
    assert a.rob([2,7,9,3,1]) == 12
    assert a.rob([1,1,1]) == 2
    assert a.rob([0]) == 0


def main():
    test()


if __name__ == "__main__":
    main()
        