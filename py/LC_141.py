class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head is not None and head.val is not None:
            head.val = None
            head = head.next
        
        if head is None:
            return False
        return True


        
def test():
    a = Solution()

    x = ListNode(3)
    x.next = ListNode(2)
    x.next.next = ListNode(0)
    x.next.next.next = ListNode(-4)
    x.next.next.next.next = x.next

    assert a.hasCycle(x) == True


if __name__ == "__main__":
    test()