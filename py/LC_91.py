class Solution:
    def numDecodings(self, s: str) -> int:
        ''' Optimal
        class Solution:
            def numDecodings(self, s: str) -> int:
                if s[0] == '0':
                    return 0
                n = len(s)
                dp = [0 for _ in range(n + 1)]
                dp[0] = 1
                for i in range(1, n + 1):
                    if s[i - 1] != '0':
                        dp[i] = dp[i - 1]
                    if i >= 2:
                        x = int(s[i - 2: i])
                        if 10 <= x <= 26:
                            dp[i] += dp[i - 2]
                return dp[n]
        '''
        
        # mine
        # time  --- O(?)
        # space --- O(n)
        cache = [0] * len(s)
        def _dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
                
            if cache[i]:
                return cache[i]
            
            cache[i] = _dfs(i + 1) + (_dfs(i + 2) if 10 <= int(s[i:i + 2]) <= 26 else 0)
                
            return cache[i]

        _dfs(0)
        return cache[0]

            

def test():
    s = Solution()

    assert s.numDecodings("1123") == 5
    assert s.numDecodings("12345") == 3
    assert s.numDecodings("120214") == 3
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("26") == 2
    assert s.numDecodings("27") == 1
    assert s.numDecodings("6120") == 1
    assert s.numDecodings("06") == 0
    assert s.numDecodings("0000000") == 0
    assert s.numDecodings("100000000") == 0
    assert s.numDecodings("6101010") == 1


def main():
    test()


if __name__ == "__main__":
    main()