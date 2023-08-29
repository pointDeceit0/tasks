class List(list):
    pass

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n + 3)
        dp2 = [0] * (n + 3)

        for i in range(n - 1, 0, -1):
            dp1[i] = max(dp1[i + 2], dp1[i + 3]) + nums[i]
        
        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 2], dp2[i + 3]) + nums[i]

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

        