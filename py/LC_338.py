class List(list):
    pass

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        j = 1
        i = 1
        while i < n + 1:
            
            while i < 2 * j and i < n + 1:
                ans.append(ans[i - j] + 1)
                i += 1
            j = i
            
        return ans
    
s = Solution()

assert s.countBits(5) == [0,1,1,2,1,2]
