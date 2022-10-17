# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        '''
        time  --- O(n)
        space --- O(1)
        '''
        prev = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev


def out(tale):
    while tale != None:
        print(tale.val, end=" ")

        tale = tale.next


def test():
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)

    b = Solution()
    b = b.reverseList(a)
    out(b)  


if __name__ == "__main__":
    test()