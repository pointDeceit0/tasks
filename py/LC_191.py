class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(str(n), 2)
        count = 0
        while n:
            if 1 & n != 0:
                count += 1
            n >>= 1
        return count
       

a = Solution()

b = int(input())
print(a.hammingWeight(b))
print(a.hammingWeight(10000000))
print(a.hammingWeight(11111111111111111111111111111101)) # 31

