class List(list):
    pass


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        time  --- O(nm)
        space --- O(n)
        '''
        
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

    assert a.wordBreak("aaaaaaa", ["aaaa","aaa"]) == True
    assert a.wordBreak("aaaaaaaaaaaaaaaa", ["aaaa","aaa", "aaaaa"]) == True
    assert a.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
    assert a.wordBreak("leetcode", ["leet","code"]) == True
    assert a.wordBreak("applepenapple", ["apple","pen"]) == True
    assert a.wordBreak("bb", ["a","b","bbb","bbbb"]) == True


if __name__ == "__main__":
    main()
        