class List(list):
    pass


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [0] + [amount + 1] * amount     
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    cache[i] = min(cache[i], cache[i - c] + 1)
        
        return cache[-1] if cache[-1] != amount + 1 else -1
                    

def main():
    sol = Solution()

    assert sol.coinChange([1, 2, 5], 100) == 20
    assert sol.coinChange([1, 7, 9], 14) == 2
    assert sol.coinChange([3, 7, 19, 21], 83) == 5
    assert sol.coinChange([2, 3, 7], 9) == 2
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1,2,5], 11) == 3
    assert sol.coinChange([2, 3, 7], 21) == 3
    assert sol.coinChange([4, 5, 9], 9) == 1
    assert sol.coinChange([4, 5, 9], 22) == 3
    assert sol.coinChange([2, 4], 7) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([186,419,83,408], 6249) == 20


if __name__ == "__main__":
    main()

