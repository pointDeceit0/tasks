class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        first, second = 1, 2
        for i in range(2, n):
            first, second = second, first + second

        return second


def main():
    a = Solution()

    assert a.climbStairs(1) == 1
    assert a.climbStairs(2) == 2
    assert a.climbStairs(3) == 3
    assert a.climbStairs(4) == 5
    assert a.climbStairs(5) == 8


if __name__ == "__main__":
    main()