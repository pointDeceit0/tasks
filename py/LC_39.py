class List(list):
    pass


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        time  --- O(n)
        space --- O(n)
        '''

        ans = []
        def __f(cur: List[int], i: int):
            if sum(cur) > target:
                return 
            elif sum(cur) == target:
                ans.append(cur)
            
            for j in range(i, len(candidates)):
                __f(cur + [candidates[j]], j)
        
        __f([], 0)
        return ans


def test():
    a = Solution()

    assert a.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
    assert a.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
    assert a.combinationSum([2], 1) == []
    assert a.combinationSum([6, 4, 2, 3, 7], 9) == [[6, 3], [4, 2, 3], [2, 2, 2, 3], [2, 7], [3, 3, 3]]
    #assert a.combinationSum() ==        
    #assert a.combinationSum() ==        


if __name__ == "__main__":
    test()