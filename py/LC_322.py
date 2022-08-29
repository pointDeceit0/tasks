from functools import lru_cache
from re import A

class List(list):
    pass


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        not efficient solution (space either)


        @lru_cache(None)
        def solution(amount, step):

            if amount == 0: return step
            if amount < 0: return -1

            steps = []
            for coin in coins:
                v = solution(amount - coin, step + 1)
                if v > 0:
                    steps.append(solution(amount - coin, step + 1)) 

            return min(steps) if len(steps) != 0 else -1

        print(solution(amount, 0))

        return solution(amount, 0)'''


        '''
        try to solve with table

        cash = [[0] + [amount + 1] * amount for i in range(len(coins) + 1)]        

        
        for i, val in enumerate(coins, start=1):
            for j in range(1, amount + 1):
                if j - val >= 0:
                    cash[i][j] = min(hash[i - 1])    

            
        return cash[-1][-1] if hash[-1][-1] != 0 or amount == 0 else -1'''

        # n - amount    m - length of coins list
        # time  --- O(n * m)
        # space --- O(n)

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
                    

def main():
    sol = Solution()

    assert sol.coinChange([186,419,83,408], 6249) == 20
    assert sol.coinChange([1, 2, 5], 100) == 20
    assert sol.coinChange([3, 7, 19, 21], 83) == 5
    assert sol.coinChange([1,2,5], 11) == 3
    assert sol.coinChange([2, 3, 7], 9) == 2
    assert sol.coinChange([2, 3, 7], 21) == 3
    assert sol.coinChange([4, 5, 9], 9) == 1
    assert sol.coinChange([4, 5, 9], 22) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([2, 4], 7) == -1
    assert sol.coinChange([1], 0) == 0


if __name__ == "__main__":
    main()

