class List(list):
    pass

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2 
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid 
        
        return min(nums[l], nums[r])
        

def test():
    a = Solution()

    assert a.findMin([3,4,5,1,2]) == min([3,4,5,1,2])
    assert a.findMin([4,5,6,7,0,1,2]) == min([4,5,6,7,0,1,2])
    assert a.findMin([11,13,15,17]) == min([11,13,15,17])
    assert a.findMin([1, 2]) == 1
    assert a.findMin([2, 1]) == 1
    assert a.findMin([1]) == 1
    assert a.findMin([2, 3, 4, 5, 6, 7, 8, 1]) == 1


def main():
    test()


if __name__ == "__main__":
    main()



