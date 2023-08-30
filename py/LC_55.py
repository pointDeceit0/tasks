class List(list):
    pass


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time  --- O(n)
        # space --- O(1)
        counter = 0
        for i in range(len(nums) - 2, -1, -1):
            counter += 1
            if nums[i] >= counter:
                counter = 0

        return True if not counter else False



def test():
    s = Solution()

    tests = [([1,2], True), ([2,0], True), ([2,3,1,1,4], True), ([1], True), ([3,2,1,0,4], False)]
    for data in tests:
        d = data[0].copy()
        res = s.canJump(data[0])
        if res == data[1]:
            print(f'Test {d}:\tDone')
        else:
            print(f'Wrong answer, get "{res}" should be "{data[1]}". Test: {d}')


def main():
    test()


if __name__ == "__main__":
    main()