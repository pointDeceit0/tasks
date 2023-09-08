class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        were = set()
        while head is not None:
            if head in were:
                return head
            were.add(head)
            head = head.next
        return None


def test():
    a = Solution()

    x = ListNode(3)
    x.next = ListNode(2)
    x.next.next = ListNode(0)
    x.next.next.next = ListNode(-4)
    x.next.next.next.next = x.next

    assert a.detectCycle(x) == x.next


if __name__ == "__main__":
    test()