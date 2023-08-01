class Solution(object):
    def containsDuplicate(self, nums):
        cache = dict()

        for v in nums:
            if v in cache:
                return True
            cache[v] = 1

        return False