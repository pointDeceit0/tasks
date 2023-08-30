from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePaths(self, m, n):
            # O(n+m)
            return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
        
        # Optimized
        # time  --- O(n*m)
        # space --- O(n)
        cur = [1] * n
        for _ in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                cur[j] = cur[j + 1] + cur[j]
        return cur[0]
        '''
        space --- O(n*m)
        with full cache

        dp =[[0] * n for _ in range(m)]

        for i in range(n):
            dp[-1][i] = 1
        for i in range(m):
            dp[i][-1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[0][0]'''

def test():
    s = Solution()

    inp_data = [[(3, 7), 28], [(3, 2), 3], [(1, 5), 1], [(6, 1), 1], [(3, 3), 6], [(6, 8), 792]]
    for data in inp_data:
        res = s.uniquePaths(*data[0])
        if res == data[1]:
            print(f'Test {data[0]}:\tDone')
        else:
            print(f'Wrong answer, get {res} should be {data[1]}. Test: {data[0]}')


def main():
    test()

if __name__ == "__main__":
    main()