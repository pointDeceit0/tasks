class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        '''
        time  --- O(n + m)
        space --- O()
        '''
        cur_list = ListNode()
        ans = cur_list

        while list1 and list2:
            if list1.val < list2.val:
                cur_list.next = list1
                list1 = list1.next
            else:
                cur_list.next = list2
                list2 = list2.next
            cur_list = cur_list.next

        if list1:
            cur_list.next = list1
        elif list2:
            cur_list.next = list2
        
        return ans.next
        '''
        ---recursive solution---
        def mergeTwoLists2(self, l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
        '''


def test():
    s = Solution()

    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))

    out = s.mergeTwoLists(a, b)
    while out:
        print(out.val, end='->')
        out = out.next
    print(None)

    


def main():
    test()

if __name__ == "__main__":
    main()