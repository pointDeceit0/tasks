import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]:
        if not lists: return None

        h = []
        heapq.heapify(h)
        for node in lists:
            while node is not None:
                heapq.heappush(h, node.val)
                node = node.next
        if not h: return None

        head = ListNode(heapq.heappop(h))
        cur = head
        while h:
            cur.next = ListNode(heapq.heappop(h))
            cur = cur.next

        return head
        


def main():
    s = Solution()
    
    # [[1,4,5],[1,3,4],[2,6]]
    n1 = ListNode(1,\
                  ListNode(4,\
                           ListNode(5)))
    n2 = ListNode(1,\
                  ListNode(3,\
                           ListNode(4)))
    n3 = ListNode(2, \
                  ListNode(6))
    ans = s.mergeKLists([n1, n2, n3])

    while ans is not None:
        print(f'{ans.val}->', end='')
        ans = ans.next
    print('None')
    
    


if __name__ == "__main__":
    main()