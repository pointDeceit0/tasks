class List(list):
    pass

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        time  --- O(n * m)
        space --- O(n)
        '''

        n, m = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, vis, prev):
            if (i, j) in vis or i == n or j == m or i < 0 or j < 0\
                or prev > heights[i][j]:
                return

            vis.add((i, j))
            dfs(i + 1, j, vis, heights[i][j])
            dfs(i, j + 1, vis, heights[i][j])
            dfs(i - 1, j, vis, heights[i][j])
            dfs(i, j - 1, vis, heights[i][j])

        for i in range(n):
            dfs(0, i, pac, heights[0][i])
            dfs(n - 1, 0, atl, heights[n - 1][i])

        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m - 1, atl, heights[i][m - 1])

        return [list(cell) for cell in atl.intersection(pac)]


def test():
    a = Solution()

    assert a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    assert a.pacificAtlantic([[1]]) == [[0, 0]]


if __name__ == "__main__":
    test()