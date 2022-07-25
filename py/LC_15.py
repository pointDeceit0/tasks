class List(list):
    pass

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        '''
        time complexity --- O(n^3)
             space      --- O(n)

        ans = []
        for f in range(n - 2):
            for s in range(f + 1, n - 1):
                for t in range(s + 1, n):
                    if (nums[f] + nums[s] + nums[t]) == 0 and all(list(per) not in ans for per in permutations((nums[f], nums[s], nums[t]), r=3)):
                        ans.append([nums[f], nums[s], nums[t]])'''

        '''
        experiments if have to return indexes of numbers

        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        nums = [(tup[1], tup[0]) for tup in nums]
        nums = dict(nums)'''

        nums.sort()
        ans = []

        '''
        time  --- O(n^2)
        space --- O(n)
        '''

        for i in range(n - 2):
            if nums[i] == nums[i - 1] and i != 0:
                # условие ломается, когда в массиве все числа одинаковые, кроме случая, когда все числа 0. 
                continue
            l, r = i + 1, n - 1

            while l != r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    cur_l = l
                    while nums[cur_l] == nums[l] and l != r:
                        l += 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

        return ans


def test():
    a = Solution()

    assert a.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert a.threeSum([]) == []
    assert a.threeSum([0]) == []
    assert a.threeSum([0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0]

test()