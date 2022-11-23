class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    class Solution:
        def hasCycle(self, head: ListNode) -> bool:
            '''
            time  --- O(n)
            space --- O(1)
            '''
            f, s = head, head

            while f and f.next:
                s = s.next
                f = f.next.next
                if f == s: return True

            return False

        
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