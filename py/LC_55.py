class List(list):
    pass


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        First version - it's very bad 
        cache = [False] * (len(nums) - 1) + [True]

        def _dp(i: int) -> None:
            if i < 0: return 
            if any(cache[i : min(len(nums) - 1, nums[i] + i) + 1]):
                cache[i] = True

            _dp(i - 1)

        _dp(len(nums) - 2)
        return cache[0]'''

        '''
        time  --- O(n)
        space --- O(1)

        nums[-1] = 1

        def _dp(i: int) -> None:
            if i < 0: return 
            for j in range(i + 1, min(len(nums) - 1, nums[i] + i) + 1):
                if nums[j]:
                    nums[i] = 1
                    break
            else:
                nums[i] = 0

            _dp(i - 1)

        _dp(len(nums) - 2)
        return nums[0]'''

        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return not goal
        



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