import random

class List(list):
    pass

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l != r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1

            elif nums[m] < nums[r]:
                r = m
            
        return nums[l]
        

def test():
    a = Solution()

    assert a.findMin([3,4,5,1,2]) == min([3,4,5,1,2])
    assert a.findMin([4,5,6,7,0,1,2]) == min([4,5,6,7,0,1,2])
    assert a.findMin([11,13,15,17]) == min([11,13,15,17])

    arr = sorted([random.randint(0, 100) for _ in range(random.randint(0, 20))])
    assert a.findMin(arr) == min(arr)
    arr = sorted([random.randint(0, 100) for _ in range(random.randint(0, 20))])
    assert a.findMin(arr) == min(arr)
    arr = sorted([random.randint(0, 100) for _ in range(random.randint(0, 20))])
    assert a.findMin(arr) == min(arr)
    arr = sorted([random.randint(0, 100) for _ in range(random.randint(0, 20))])
    assert a.findMin(arr) == min(arr)
    arr = sorted([random.randint(0, 100) for _ in range(random.randint(0, 20))])
    assert a.findMin(arr) == min(arr)


test()
print('worked')