class List(list):
    pass

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        '''
        Time limited exceeded

        time  O(n^2)
        space O(n)

        squares = []
        for i in range(n - 1):
            m = 0
            for j in range(i + 1, n):
                m = max(m, (j - i) * min(height[i], height[j]))

            squares.append(m)

        return max(squares)'''

        '''
        on leetcode shows that memory storaged is more when you use variable with max value of square instead of array of squares, 
        but to be logical it is wrong because with array memory complexity is n, but with variable 1

        time  --- O(n)
        space --- O(1)

        '''

        l, r = 0, n - 1

        square = (r - l) * min(height[l], height[r])
        while l < r:
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            
            square = max((r - l) * min(height[l], height[r]), square)

        return square

def test():
    a = Solution()

    assert a.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert a.maxArea([1,1]) == 1
    assert a.maxArea([5, 2, 3, 7, 4, 2, 5]) == 30

test()
