class List(list):
    pass

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        100% beats memory solution
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

        for i in range(m):
            dfs(0, i, pac, heights[0][i])
            dfs(n - 1, i, atl, heights[n - 1][i])

        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m - 1, atl, heights[i][m - 1])

        return [list(cell) for cell in atl.intersection(pac)]
        '''
        # mine
        heights = [[0] * (len(heights[0]) + 2)] + \
                  [[0] + row + [0] for row in heights] + \
                  [[0] * (len(heights[0]) + 2)]
        
        m, n = len(heights), len(heights[0])
        ways = [[0] * n for _ in range(m)]

        def _dfs(x: int, y: int, were: set):
            # 0 - nothing, 1 - Pacific, 2 - Atlantic, 3 - both
            if (x, y) in were:
                return ways[x][y]
            
            if x == 0 or y == 0:
                return 1
            if x == m - 1 or y == n - 1:
                return 2
            
            if ways[x][y] == 3:
                return ways[x][y]
            
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if heights[x + i][y + j] <= heights[x][y]:
                    were.add((x, y))
                    ways[x][y] |= _dfs(x + i, y + j, were)

            return ways[x][y]
            
        ans = []
        for i in range(1, m):
            for j in range(1, n):
                if ways[i][j] != 3:
                    _dfs(i, j, set())
                if ways[i][j] == 3:
                    ans.append([i - 1, j - 1])
        
        return ans


def test():
    a = Solution()

    assert a.pacificAtlantic([[3,3,3],[3,1,3],[0,2,4]]) == [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
    assert a.pacificAtlantic([[1,1],[1,1],[1,1]]) == [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
    assert a.pacificAtlantic([[1]]) == [[0, 0]]
    assert a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


if __name__ == "__main__":
    test()