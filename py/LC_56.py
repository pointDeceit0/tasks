class List(list):
    pass

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ''' My solution
        time  --- O(n) + O(nlogn)
        space --- O(n)
        '''
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        i = 0
        while i != len(intervals):
            cur = intervals[i]
            while i + 1 != len(intervals) and cur[1] >= intervals[i + 1][0]:
                cur[1] = max(cur[1], intervals[i + 1][1])
                i += 1
            ans.append(cur)
            i += 1
        return ans

        ''' Beauty solution
        same
        '''
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
        

def test():
    s = Solution()

    assert s.merge([[1,100],[2,3],[56,64]]) == [[1,100]]
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert s.merge([[1,4],[4,5]]) == [[1,5]]
    assert s.merge([[1,3],[2,6],[5,10],[9,12]]) == [[1,12]]
    assert s.merge([[1,100],[2,3],[56,64], [78,104]]) == [[1,104]] 
    assert s.merge([[0,0]]) == [[0,0]] 

def main():
    test()

    
if __name__ == "__main__":
    main()