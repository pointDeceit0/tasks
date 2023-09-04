class List(list):
    pass


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def _dfs(y: int, x: int) -> None:
            grid[y][x] = '0'
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not(y + i < 0 or x + j < 0 or y + i == len(grid) or x + j == len(grid[0]) or not (grid[y + i][x + j] == '1')):
                    _dfs(y + i, x + j)


        counter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    counter += 1
                    _dfs(y, x)

        return counter


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
    ]) == 0
    assert a.numIslands([
                      [],
                      [],
                      []
    ]) == 0
    assert a.numIslands([]) == 0

    
if __name__ == "__main__":
    test()