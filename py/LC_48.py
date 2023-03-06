class List(list):
    pass


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        time  --- O(n^2)
        space --- O(1)
        """
        n = len(matrix) - 1
        for i in range((n + 1) // 2):
            for j in range(i, n - i):
                cur1, cur2 = matrix[i][j], matrix[n - i][n - j]

                matrix[i][j]         = matrix[n - j][i]
                matrix[n - i][n - j] = matrix[j][n - i] 
                matrix[j][n - i] = cur1 
                matrix[n - j][i] = cur2
        
        print(*matrix, sep='\n')
        return matrix
              


def test():
    s = Solution()

    assert s.rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    assert s.rotate([[1,2],[3,4]]) == [[3,1],[4,2]]


def main():
    test()


if __name__ == "__main__":
    main()