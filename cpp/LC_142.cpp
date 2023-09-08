#include <iostream>
#include <set>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        std::set<ListNode*> were;

        while (head != nullptr) {
            if (were.count(head)) {
                return head;
            }
            were.insert(head);
            head = head->next;
        }
        return nullptr;
    }
};