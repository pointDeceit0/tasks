from bisect import bisect_left


class List(list):
    pass


class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int:

        # With binary search
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x) 
                sub[idx] = x 
        return len(sub)

        '''
        the most common
        dp = [1] + [0] * (len(nums) - 1)

        for i in range(1, len(nums)):
            temp = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    temp = max(dp[j], temp)
            dp[i] = temp + 1
        
        return max(dp)'''
        
        '''
        mine
        dp = []
        for v in nums:
            cur = [v]
            for seq in dp:
                if v > seq[-1]:
                    cur = max(seq + [v], cur, key=len)
            dp.append(cur)
        
        return len(max(dp, key=len))'''


def test():
    s = Solution()

    response = s.lengthOfLIS([0,1,0,3,2,3])         
    assert response == 4, response
    response = s.lengthOfLIS([10,9,2,5,3,7,101,18])
    assert response == 4, response
    response = s.lengthOfLIS([7,7,7,7,7,7,7])       
    assert response == 1, response


def main():
    test()


if __name__ == "__main__":
    main()