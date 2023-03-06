class Solution:
    def isValid(self, s: str) -> bool:
        '''
        time  --- O(n)
        space --- O(n)
        '''
        left = []

        for par in s:
            if par in {"(", "[", "{"}:
                left.append(par)
            elif not left:
                return False
            else:
                cur = left.pop()
                if cur == "(" and par == ")" or cur == "[" and par == "]" or cur == "{" and par == "}":
                    continue
                else:
                    return False

        return True if not left else False
        '''
        ---solution with dictionary---
        class Solution(object):
	        def isValid(self, s):
                """
                :type s: str
                :rtype: bool
                """
                d = {'(':')', '{':'}','[':']'}
                stack = []
                for i in s:
                    if i in d:  # 1
                        stack.append(i)
                    elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                        return False
                return len(stack) == 0 # 3
        '''


def test():
    s = Solution()

    tests = (("()", True), ("()[]{}", True), ("[)", False))
    for data in tests:
        res = s.isValid(data[0])
        if res == data[1]:
            print(f'Test "{data[0]}":\tDone')
        else:
            print(f'Wrong answer, get "{res}" should be "{data[1]}". Test: {data[0]}')


def main():
    test()


if __name__ == "__main__":
    main()