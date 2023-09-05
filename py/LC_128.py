class List(list):
    pass


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''class Solution:
            def longestConsecutive(self, nums: List[int]) -> int:
                longest = 0
                num_set = set(nums)
        
                for n in num_set:
                    if (n-1) not in num_set:
                        length = 1
                        while (n+length) in num_set:
                            length += 1
                        longest = max(longest, length)
                
                return longest'''
        nodes = {}

        for n in nums:
            if n - 1 in nodes:
                nodes[n - 1] = n
            if n + 1 in nodes:
                nodes[n] = n + 1
            else:
                nodes[n] = None

        ans = 0
        for n in nodes:
            if nodes[n] is None:
                cur = 0
                while n in nodes:
                    n -= 1
                    cur += 1
                ans = max(ans, cur)
        return ans


def test():
    s = Solution()

    assert s.longestConsecutive([100,4,200,1,3,2])     == 4
    assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9


def main():
    test()


if __name__ == "__main__":
    main()