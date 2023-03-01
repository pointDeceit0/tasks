import string


class Solution:
    encode = {str(i): v for i, v in enumerate(string.ascii_uppercase, 1)}

    def numDecodings(self, s: str) -> int:
        '''
        time  --- O(n)
        space --- O(n)
        '''
        cache = [-1] * (len(s) - 1)

        def _dp(i: int):
            if i >= len(s) - 1:
                if i == len(s) - 1 and s[i] == "0":
                    return 0
                return 1
            # if in cache
            if cache[i] != -1: return cache[i]
            
            # _ case and _._ case
            cache[i] = (_dp(i + 1) if s[i : i + 1] in self.encode else 0) + \
                       (_dp(i + 2) if s[i : i + 2] in self.encode else 0)
            
            return cache[i]

        return _dp(0)
                

def test():
    s = Solution()

    assert s.numDecodings("12345") == 3
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