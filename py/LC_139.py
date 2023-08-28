class List(list):
    pass


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def _dfs(st) -> bool:


            if not st: return True
            
            for w in wordDict:
                l_w = len(w)
                l_st = len(st)
                if l_st >= l_w and st[l_st - l_w:] == w:
                    res = _dfs(st[l_w:])
                    if res:
                        return True
            return False
        

        dp = [0] * len(s) + [1]

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                
        return bool(dp[0])


def main():
    a = Solution()

    assert a.wordBreak("leetcode", ["leet","code"]) == True
    print('4 pass')
    assert a.wordBreak("aaaaaaa", ["aaaa","aaa"]) == True
    print('1 pass')
    assert a.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
    print('3 pass')
    assert a.wordBreak("aaaaaaaaaaaaaaaa", ["aaaa","aaa", "aaaaa"]) == True
    print('2 pass')
    assert a.wordBreak("applepenapple", ["apple","pen"]) == True
    print('5 pass')
    assert a.wordBreak("bb", ["a","b","bbb","bbbb"]) == True
    print('6 pass')


if __name__ == "__main__":
    main()
        