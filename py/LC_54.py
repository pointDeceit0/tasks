class List(list):
    pass

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        time  --- O(n*m)
        space --- O(n*m)
        '''

        r, c = 0, 0
        ans = []
        num = len(matrix) * len(matrix[0])
        while num != 0:
            # from left to right, top
            for i in range(c, len(matrix[0]) - c):
                ans.append(matrix[r][i])
                num -= 1

            if num == 0: return ans
            # from top to bottom, right
            for i in range(1 + r, len(matrix) - r):
                ans.append(matrix[i][len(matrix[0]) - 1 - c])
                num -= 1

            if num == 0: return ans
            # from left to right, bottom
            for i in range(len(matrix[0]) - 2 - c, c - 1, -1):
                ans.append(matrix[len(matrix) - 1 - r][i])
                num -= 1

            if num == 0: return ans
            # from bottom to top, left
            for i in range(len(matrix) - 2 - r, r, -1):
                ans.append(matrix[i][c])
                num -= 1
            
            r += 1
            c += 1
        
        return ans


def test():
    s = Solution()

    assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    #assert s.spiralOrder() ==


def main():
    test()

if __name__ == "__main__":
    main()