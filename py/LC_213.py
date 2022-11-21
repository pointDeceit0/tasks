class List(list):
    pass

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        time  --- O(n)      but actually O(n) + O(n) + creation. It's important here, i think
        space --- O(n)
        '''
        if len(nums) < 4: return max(nums)
        dp1, dp2 = [0] * (len(nums) + 3), [0] * (len(nums) + 3)

        for i in range(len(nums) - 1, 0, -1):
            dp1[i] = max(nums[i] + dp1[i + 3], nums[i] + dp1[i + 2])

        for i in range(3, len(nums) + 2):
            dp2[i] = max(nums[i - 3] + dp2[i - 3], nums[i - 3] + dp2[i - 2])

        return max(max(dp1), max(dp2))


def test():
    a = Solution()

    assert a.rob([2, 7, 9, 3, 1]) == 11
    assert a.rob([1, 2, 3, 1]) == 4
    assert a.rob([1, 2, 3]) == 3
    assert a.rob([2, 3, 2]) == 3
    assert a.rob([11, 7, 3, 5, 0, 1, 8, 3, 2]) == 24
    assert a.rob([11, 7, 3, 5, 0, 1, 8, 3]) == 24


if __name__ == "__main__":
    test()

        