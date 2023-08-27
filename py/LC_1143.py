class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # It seems to be O(n*m) similar to solution below, 
        # but indeed it's quite slower. Why? Hidden constants
        def _dfs(i: int, j: int) -> None:
            nonlocal dp

            if i == n or j == m:
                return 0
            
            if dp[j][i]:
                return dp[j][i]
            
            if text1[i] == text2[j]:
                dp[j][i] = 1 + _dfs(i + 1, j + 1)
                return dp[j][i]
            
            dp[j][i] = max(_dfs(i + 1, j), _dfs(i, j + 1))
            return dp[j][i]
            

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]


def test():
    s = Solution()

    assert s.longestCommonSubsequence('abcde', 'ace') == 3
    assert s.longestCommonSubsequence('abc', 'def')   == 0
    assert s.longestCommonSubsequence('ababa', 'ababa') == 5
    assert s.longestCommonSubsequence('abc', 'abc')   == 3
    assert s.longestCommonSubsequence("ac", "dc")     == 1

    assert s.longestCommonSubsequence("bmvcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq", "bmpmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx")   == 13
    assert s.longestCommonSubsequence("bmvcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq", "bmpmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx")   == 13
    assert s.longestCommonSubsequence("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl")   == 6
    assert s.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg")               == 3
    assert s.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr")                   == 5
    
    assert s.longestCommonSubsequence("xaxx", "a")          == 1
    assert s.longestCommonSubsequence('aaaaa', 'a')         == 1
    assert s.longestCommonSubsequence("gbcba", "abcbcdag")  == 4
    assert s.longestCommonSubsequence("abcba", "abcbcba")   == 5


    assert s.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert s.longestCommonSubsequence("ezupkr", "ubmrapg")     == 2
    assert s.longestCommonSubsequence('bbb', '')               == 0
    assert s.longestCommonSubsequence('', 'b')                 == 0
    

if __name__ == "__main__":
    test()