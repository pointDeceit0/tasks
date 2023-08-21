from collections import defaultdict

class List(list):
    pass

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # some fast shit
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1
        
        result = []
        if zeros:
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))       
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result
    
    class Solution:
        def threeSum1(self, nums: List[int]) -> List[List[int]]:
            # Mine one 
            ans = []
            nums.sort()
            prev_v = None

            for i in range(len(nums)):
                if nums[i] == prev_v:
                    continue
                l, r = i + 1, len(nums) - 1
                prev_l = None

                while l < r:
                    if nums[l] == prev_l or nums[i] + nums[l] + nums[r] < 0:
                        prev_l = nums[l]
                        l += 1
                        continue
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                        continue

                    elif nums[i] + nums[l] + nums[r] == 0:
                        ans.append([nums[i], nums[l], nums[r]])

                        prev_l = nums[l]
                prev_v = nums[i]

            return ans



def test():
    a = Solution()

    assert a.threeSum([3,0,-2,-1,1,2]) == [[3, -2, -1], [0, -2, 2], [0, -1, 1]]
    assert a.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert a.threeSum([0, 0, 0, 0, 0, 0, 0, 0]) == [[0, 0, 0]]
    assert a.threeSum([]) == []
    assert a.threeSum([0]) == []

test()