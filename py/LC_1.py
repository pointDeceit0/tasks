class Solution(object):
    def twoSum(self, nums, target):
        cache = dict()

        for i, v in enumerate(nums):
            if v in cache:
                return [cache[v], i]
            cache[target - v] = i
        

def test():
    s = Solution()

    assert s.twoSum([2,7,11,15], 9) == [0, 1]
    assert s.twoSum([3,2,4], 6) == [1, 2]
    assert s.twoSum([3,3], 6) == [0, 1]


def main():
    test()


if __name__ == "__main__":
    main()