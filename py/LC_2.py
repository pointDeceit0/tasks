class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        dummy = ListNode()
        
        cur_node = dummy
        extra = 0
        
        while l1 or l2:
            cur_sum = extra
            
            if l1:
                cur_sum += l1.val
                l1 = l1.next
                
            if l2:
                cur_sum += l2.val
                l2 = l2.next
                
            cur_node.next = ListNode(cur_sum % 10)
            cur_node = cur_node.next
            extra = cur_sum // 10
            
        if extra > 0:
            cur_node.next = ListNode(extra)
            
        return dummy.next
                
        

a = Solution()

print(a.addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(a.addTwoNumbers([9,9,9,9], [9,9,9,9,9,9,9]))