class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        O( n^2 )

        delta = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > delta:
                    delta = prices[j] - prices[i]
        return delta
        
        '''

        '''
        for i in range(len(prices)):
            if (prices[i] < prices[s] or i + 1 == len(prices)) and i - s != 0:
                delta = m - prices[s] if m - prices[s] > delta else delta
                s = i
                m = 0
            
            m = prices[i] if prices[i] > m else m
        
        '''
        
        s, delta = 0, 0
        i = 1

        while i < len(prices):
            cur_delta = prices[i] - prices[s]
            if prices[i] > prices[s]:
                delta = max(delta, cur_delta)
            else:
                s = i
            i += 1

        return delta



a = Solution()

print(a.maxProfit([1, 2]))
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))
#print(a.maxProfit())

        