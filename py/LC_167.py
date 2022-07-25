class List(list):
    pass


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 1: return -1

        n = len(numbers)
        
        l, r = 0, n - 1

        while l != r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            elif numbers[l] + numbers[r] > target:
                r -= 1

            elif numbers[r] + numbers[l] < target:
                l += 1


def test():
    a = Solution()

    assert a.twoSum([2,7,11,15], 9) == [1, 2]
    assert a.twoSum([2,3,4], 6) == [1, 3]
    assert a.twoSum([-1, 0], -1) == [1, 2]
    assert a.twoSum([0], 0) == -1


def main():
    test()

if __name__ == "__main__":
    main()