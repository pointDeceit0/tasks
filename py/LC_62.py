class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        time  --- O(n * m)
        space --- O(n)
        '''
        cur, prev = [1] * n, [1] * n
        
        for _ in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                cur[j] = prev[j] + cur[j + 1]    
            prev, cur = cur, [1] * n
        
        return prev[0]


def test():
    s = Solution()

    inp_data = [[(3, 7), 28], [(3, 2), 3], [(1, 5), 1], [(6, 1), 1], [(3, 3), 6], [(6, 8), 792]]
    for data in inp_data:
        res = s.uniquePaths(*data[0])
        if res == data[1]:
            print(f'Test {data[0]}:\tDone')
        else:
            print(f'Wrong answer, get {res} should be {data[1]}. Test: {data[0]}')


def main():
    test()

if __name__ == "__main__":
    main()