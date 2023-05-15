class Solution:
    '''
    The fastest I've found. Similar to mine is half, but more accurate and correspondingly faster.
    '''
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=len)
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    '''
    Not mine but very beautiful solution, suddenly, it doesn't work so well also
    '''
    def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom
    
    '''
    Mine is half
    '''
    def longesPalindrome(self, s: str) -> str:

        if len(s) == 0: return ''

        n = len(s)
        max_pal = ''

        for i in range(n):
            j = 0
            
            a, b = 0, 0
            while i - j >= 0 and i + j < n:
                cur = s[i - j : i + j + 1]
                cur_even = s[i - j : i + j + 2]
                
                if cur == cur[::-1] and not a:
                    max_pal = max(max_pal, cur, key=lambda x: len(x))
                else:
                    a = 1
                
                if cur_even == cur_even[::-1] and not b:
                    max_pal = max(max_pal, cur_even, key=lambda x: len(x))
                else: 
                    b = 1

                if a and b:
                    break

                j += 1
                
            '''
            j = 0
            cur_even = s[i] + s[i + 1]
            while i - j >= 0 and i + j < n:
                cur_even = s[i - j : i + j + 2]

                if cur_even == cur_even[::-1]:
                    max_pal = max(max_pal, cur_even, key=lambda x: len(x))

                j += 1'''
                
        return max_pal

        '''
        Mine, but too slow

        if len(s) == 0: return ""
        
        max_pal = ''
        n = len(s)
        layers_check = [0] * n

        def _dps(comb: str, layer: int) -> None:
            nonlocal max_pal
            if len(comb) == 1:
                if layers_check[layer]:
                    return 
                layers_check[layer] = 1

            if comb == comb[::-1]:
                # get max string by the length of it 
                max_pal = max(max_pal, comb, key=lambda x: len(x)) 

            # if layer bigger than beginning array
            if layer + 1 == n: return
            
            _dps(comb + s[layer + 1], layer + 1)
            _dps(s[layer + 1], layer + 1)

            return

        _dps(s[0], 0)

        return max_pal'''
            

def test():
    s = Solution()

    assert s.longestPalindrome("ababcba") == "abcba"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("") == ""

    assert s.longestPalindrome("ababacdfgfdc") == "cdfgfdc"
    assert s.longestPalindrome("ababacdfgfdcaba") == "abacdfgfdcaba"


def main():
    test()


if __name__ == "__main__":
    main()