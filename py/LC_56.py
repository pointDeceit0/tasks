class List(list):
    pass

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ans = []
        overlap_int = intervals[0]
        for int in intervals[1:]:
            if int[0] > overlap_int[1]:
                ans.append(overlap_int)
                overlap_int = int
            else:
                overlap_int[1] = max(overlap_int[1], int[1])
        ans.append(overlap_int)
        return ans 
                

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