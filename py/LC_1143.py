class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time  --- O(mn)
        Space --- O(mn)
        '''
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, - 1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]


        
        # attempt to solve the problem for O(n) memory
        cur = [0] * (n + 1)
        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1):
                #                 Условие проверяет не на то ли же самое место ставится символ в последовательности
                if text1[j] == text2[i] and cur[j + 1] == cur[j]:
                    cur[j] += 1
                else:
                    cur[j] = max(cur[j + 1], cur[j])
        
        return max(cur)


    def longestCommonSubsequenceTimeExceeded(self, text1: str, text2: str) -> int:
        '''It works(i suppose) but Time limited exceeded

        Time  --- O(nm^2)
        Space --- O(nm)'''

        if len(text1) == 0 or len(text2) == 0: return 0

        seq = text1 if len(text1) > len(text2) else text2
        sub = text2 if len(text1) > len(text2) else text1

        n, m = len(seq), len(sub)
        dp = [[0] * m for _ in range(n)]

        ans = 0
        for i, ch_seq in enumerate(seq):
            for j, ch_sub in enumerate(sub):
                if ch_seq == ch_sub:
                    dp[i][j] = 1
                    ans = 1

        # идти снизу вверх и смотреть самые возрастающие подпоследовательности
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                
                if dp[j][i]:
                    m = 0
                    for h in range(n - 1, j, -1):
                        m = max(m, dp[h][i + 1])
                    dp[j][i] = m + 1

                    ans = max(m + 1, ans)
                else:
                    m = 0
                    # Here's j - 1, 'cause it can be at the same position in the next iter
                    for h in range(n - 1, j - 1, -1):
                        m = max(m, dp[h][i + 1])
                    dp[j][i] = m
        print(*dp, sep='\n')
        print()
        return ans            


def test():
    s = Solution()

    assert s.longestCommonSubsequenceTimeExceeded("bmvcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq", "bmpmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx")   == 13
    assert s.longestCommonSubsequence("bmvcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq", "bmpmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx")   == 13
    assert s.longestCommonSubsequence("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl")   == 6
    assert s.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg")               == 3
    assert s.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr")                   == 5
    
    assert s.longestCommonSubsequence("xaxx", "a")          == 1
    assert s.longestCommonSubsequence('aaaaa', 'a')         == 1
    assert s.longestCommonSubsequence("gbcba", "abcbcdag")  == 4
    assert s.longestCommonSubsequence("abcba", "abcbcba")   == 5

    assert s.longestCommonSubsequence('abc', 'def')   == 0
    assert s.longestCommonSubsequence('abcde', 'ace') == 3
    assert s.longestCommonSubsequence('abc', 'abc')   == 3
    assert s.longestCommonSubsequence("ac", "dc")     == 1

    assert s.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert s.longestCommonSubsequence("ezupkr", "ubmrapg")     == 2
    assert s.longestCommonSubsequence('bbb', '')               == 0
    assert s.longestCommonSubsequence('', 'b')                 == 0
    

if __name__ == "__main__":
    test()