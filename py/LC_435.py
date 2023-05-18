class List(list):
    pass


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        prev_end = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
                continue
            else:
                res += 1
                prev_end = min(end, prev_end)
        
        return res


def test():
    s = Solution()

    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2 
    assert s.eraseOverlapIntervals([[1,2],[2,3]]) == 0 
    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[0,2]]) == 1 
    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,7],[4,7]]) == 1
    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,7],[3,6]]) == 1 
    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,7],[3,7]]) == 1
    assert s.eraseOverlapIntervals([[1,100], [1, 11], [2, 12], [11,22]]) == 2


if __name__ == "__main__":
    test()