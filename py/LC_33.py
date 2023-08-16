class List(list):
    pass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        if target == nums[r]:
            return r

        return -1
    

def test():
    s = Solution()

    assert s.search([4, 5, 6, 7, 8, 1, 2], 8) == 4
    assert s.search([4,5,6,7,0,1,2], 6) == 2
    assert s.search([1], 1) == 0
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    assert s.search([4,5,6,7,0,1,2], 3) == -1
    assert s.search([1], 0) == -1


def main():
    test()


if __name__ == "__main__":
    main()
