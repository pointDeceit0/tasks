class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(16):
            x, y = int('1' + '0'*i, 2), int('1' + '0'*(31 - i), 2)
            x &= n
            y &= n
            x <<= 31 - i * 2
            y >>= 31 - i * 2
            ans |= x
            ans |= y
        
        return ans

        '''
        similar to mine but shorter and better
        public class Solution {
            public int reverseBits(int n) {
                int reversed = 0; 
                for (int i = 0; i < 32; i++) {

                    reversed <<= 1; 

                    reversed += n & 1; 

                    n >>= 1; 
                }

                return reversed;
            }
        }'''


s = Solution()
print(len('00000010100101000001111010011100'))
assert s.reverseBits(43261596) == 964176192 
# 00000010100101000001111010011100

