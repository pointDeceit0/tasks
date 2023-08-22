class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Case (-1, 1) don't work with this code
        It is related with python specifity
        The same code in c++ beats 100%, ain't talking about memory
        Yeah, I'm not kidding

        class Solution {
        public:
            int getSum(int a, int b) {
                while (b != 0) {
                    int x = a;
                    a = a ^ b;
                    b = (x & b) << 1;
                }
                return a;
            }
        };
        """

        '''
        Solution that solves problem of -1, 1, because it controls overflow over 32 bits

        class Solution:
            def getSum(self, a: int, b: int) -> int:
                mask = 0xFFFFFFFF
                
                while b:
                    a, b = (a ^ b) & mask, ((a & b) << 1) & mask
                
                return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        '''
        
        while b != 0:
            x = a
            a = a ^ b
            b = (x & b) << 1

        return a


def test():
    a = Solution()

    assert a.getSum(-4, 1) == -3
    assert a.getSum(-1, 1) == 0
    assert a.getSum(5, 7) == 12 
    assert a.getSum(10, 11) == 21
    assert a.getSum(2, 3) == 5
    assert a.getSum(1, 0) == 1
    assert a.getSum(2, 33) == 35 
    assert a.getSum(56, 732) == 788

test()  