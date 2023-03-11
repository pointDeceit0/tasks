class List(list):
    pass


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]: 
        
        ans = []
        for i, int in enumerate(intervals):
            if int[1] < new_interval[0]:
                ans.append(int)

            elif int[0] > new_interval[1]:
                ans.append(new_interval)
                return ans + intervals[i:]

            else:
                new_interval[0] = min(new_interval[0], int[0])
                new_interval[1]   = max(new_interval[1], int[1])
        ans.append(new_interval)
        return ans


        '''if not intervals: return [new_interval]

        for i in range(len(intervals)):
            if new_interval[0] <= intervals[i][1] and intervals[i][1] <= new_interval[1] \
                or new_interval[1] >= intervals[i][0] and intervals[i][1] >= new_interval[1]:

                j = i
                while i < len(intervals) and new_interval[1] >= intervals[i][0]:
                    i += 1
                return intervals[:j] \
                        + [[min(intervals[j][0], new_interval[0]), max(intervals[i - 1][1], new_interval[1])]] \
                        + intervals[i:]
            
            # in this case we don't do any check with prev, because cond. above would work on prev. step
            elif intervals[i][0] > new_interval[1]: 
                return intervals[:i] + [new_interval] + intervals[i:]
            
            # if new_el is more than current in ints, we check next on intersection
            elif new_interval[0] > intervals[i][1]: 
                if not(len(intervals) - i - 1 and new_interval[1] >= intervals[i + 1][0]):
                    return intervals[:i + 1] + [new_interval] + intervals[i + 1:]'''
            


def test():
    s = Solution()

    assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert s.insert([[1,4]],[6,8]) == [[1,4],[6,8]]
    assert s.insert([[1,5]],[0,0]) == [[0,0],[1,5]]
    assert s.insert([], [2,5]) == [[2,5]]
    assert s.insert([[1,2],[5,6],[8,10]],[4,9]) == [[1,2],[4,10]]
    assert s.insert([[3,4],[6,7]],[1,10]) == [[1,10]]


def main():
    test()


if __name__ == "__main__":
    main()
