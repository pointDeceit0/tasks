class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        #O( n log(n + m) )

        nums1.extend(nums2)
        nums = sorted(nums1)

        match len(nums) % 2:
            case 0:
                return (nums[(len(nums) - 1) // 2] + nums[(len(nums) - 1) // 2 + 1]) / 2
            case _:
                return nums[(len(nums) - 1) // 2]'''

        # O( log(min(n + m)) )

        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(nums1) - 1

        while True:
            m = (l + r) // 2
            j = half - m - 2 # pointer for array nums 1, because array starts with zero

            l1 = nums1[m] if m >= 0 else float('-infinity')
            r1 = nums1[m + 1] if (m + 1) < len(nums1) else float('infinity')
            l2 = nums2[j] if j >= 0 else float('-infinity')
            r2 = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = m - 1
            else:
                l = m + 1

a = Solution()

print(a.findMedianSortedArrays([1, 2], [3, 4]))
print(a.findMedianSortedArrays([1, 3], [2]))
print(a.findMedianSortedArrays([1], [1]))
print(a.findMedianSortedArrays([1, 1, 1], [1]))
        