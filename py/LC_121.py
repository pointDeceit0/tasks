class Solution(object):
    def maxProfit(self, prices):
        
        target = prices[0]
        max_dif = 0

        for i in range(1, len(prices)):
            if prices[i] < target:
                target = prices[i]
            elif prices[i] - target > max_dif:
                max_dif = prices[i] - target

        return max_dif


def test():
    s = Solution()

    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0


def main():
    test()


if __name__ == "__main__":
    main()