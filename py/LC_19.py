class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Perfectum:
        
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
        '''

        # time  --- O(n)
        # space --- O(1)
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        head = prev

        prev = None
        for _ in range(n - 1):
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        head = head.next
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev


def main():
    s = Solution()

    n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    ans = s.removeNthFromEnd(n, 2)

    while ans is not None:
        print(f'{ans.val}->', end='')
        ans = ans.next
    print('None')
            

if __name__ == "__main__":
    main()