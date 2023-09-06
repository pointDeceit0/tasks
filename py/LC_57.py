class List(list):
    pass


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]: 
        '''
        prettier than mine below
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
        '''
        # time  --- O(n)
        # space --- O(n)
        ans = []

        inserted = True
        for i, int in enumerate(intervals):
            if new_interval[0] <= int[1]:
                inserted = False
                start = min(new_interval[0], int[0])
                while i + 1 < len(intervals) and new_interval[1] >= intervals[i][1]:
                    i += 1
                if intervals[i][0] > new_interval[1]:
                    ans.append([start, new_interval[1]])
                else:
                    ans.append([start, max(new_interval[1], intervals[i][1])])
                    i += 1
                break
            ans.append(int)
        
        if inserted:
            if len(intervals) > 0 and new_interval[1] < intervals[0][0]:
                ans = [new_interval] + ans
            else:
                ans += [new_interval]
        else:
            ans.extend(intervals[i:])
        
        return ans


def test():
    s = Solution()

    assert s.insert([[3,4],[6,7]],[1,10]) == [[1,10]]
    assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert s.insert([[1,5]],[0,0]) == [[0,0],[1,5]]
    assert s.insert([[1,4]],[6,8]) == [[1,4],[6,8]]
    assert s.insert([], [2,5]) == [[2,5]]
    assert s.insert([[1,2],[5,6],[8,10]],[4,9]) == [[1,2],[4,10]]


def main():
    test()


if __name__ == "__main__":
    main()
