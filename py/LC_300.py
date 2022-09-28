class List(list):
    pass


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        """
        time  --- O(n^2)
        space --- O(n)
        """        

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

"""
there's solution with O(nlogn) time complexity
but it's quite more difficult
"""


def test():
    s = Solution()

    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,3,2,3])         == 4
    assert s.lengthOfLIS([7,7,7,7,7,7,7])       == 1


def main():
    test()


if __name__ == "__main__":
    main()