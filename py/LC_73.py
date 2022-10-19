class List(list):
    pass


class Solution:
    '''
    time --- O(n*m)
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        space --- O(n + m)
        '''

        rows, columns = set(), set()
        
        for i, _ in enumerate(matrix): # rows
            for j, v in enumerate(matrix[i]): # columns
                if v == 0:
                    rows.add(i)
                    columns.add(j)

        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for i in columns:
            for j in range(len(matrix)):
                matrix[j][i] = 0


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        space --- O(1)
        """
        n, m = len(matrix), len(matrix[0])
        zero = False

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0: matrix[row][0] = 0
                    else: zero = True

        for row in range(1, n):
            for col in range(1, m):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(n):
                matrix[row][0] = 0
        if zero:
            for col in range(m):
                matrix[0][col] = 0


def test():
    a = Solution()

    assert a.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    assert a.setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]


if __name__ == "__main__":
    test()
        