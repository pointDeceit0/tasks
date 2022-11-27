class List(list):
    pass


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        time  --- O(n*m)
        space --- O(1), because caching in-place
        '''
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            # check if outside the field
            if (i == n or j == m or i < 0 or j < 0 or grid[i][j] == "0"): return True

            # check if already was here
            if grid[i][j] == "2": return True
            # check if current island and mark that was here
            if grid[i][j] == "1": grid[i][j] = "2"

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            
            # it is the moment, when tracker returns to start position, he went all over the island 
            return False

        ans = 0
        for i in range(n):
            for j in range(m):
                if not dfs(i, j):
                    ans += 1

        return ans


def test():
    a = Solution()

    assert a.numIslands([
                      ["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]
                    ]) == 1
    assert a.numIslands([
                      ["1","1","0","0","0"],
                      ["1","1","0","0","0"],
                      ["0","0","1","0","0"],
                      ["0","0","0","1","1"]
                    ]) == 3
    assert a.numIslands([
                      ['1'],
                      ['0'],
                      ['1']
                    ]) == 2
    assert a.numIslands([
                      ['0'],
                      ['1'],
                      ['0']
                    ]) == 1
    assert a.numIslands([
                      ['1', '0', '1', '1']
    ]) == 2
    assert a.numIslands([
                      ['0', '1', '0', '0']
    ]) == 1
    assert a.numIslands([
                      []
    ])
    assert a.numIslands([
                      [],
                      [],
                      []
    ]) == 0
    assert a.numIslands([]) == 0

    
if __name__ == "__main__":
    test()