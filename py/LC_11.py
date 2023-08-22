class List(list):
    pass

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area


def test():
    a = Solution()

    assert a.maxArea([1,3,2,5,25,24,5]) == 24
    assert a.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert a.maxArea([1,1]) == 1
    assert a.maxArea([5, 2, 3, 7, 4, 2, 5]) == 30

test()
