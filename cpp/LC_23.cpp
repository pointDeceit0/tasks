#include <vector>
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        // Time  --- O(2t(lists[0] + ... + lists[t])) -> O(t^2 * avgLen(lists))
        ListNode* head = nullptr;
        int start;
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i] != nullptr) {
                head = lists[i];
                start = i;
                break;
            }
        }
        if (head == nullptr) {
            return nullptr;
        }
        
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i] != nullptr) {
                if (lists[i]->val < head->val) {
                    head = lists[i];
                    start = i;
                }
            }
        }
        lists[start] = lists[start]->next;
        head->next = mergeKLists(lists);
        return head;
    }
};


int main() {
    ListNode n1(1);
    ListNode n2(4);
    ListNode n3(5);
    n2.next = &n3;
    n1.next = &n2;

    ListNode h1(1);
    ListNode h2(3);
    ListNode h3(4);
    h2.next = &h3;
    h1.next = &h2;

    ListNode g1(2);
    ListNode g2(6);
    g1.next = &g2;

    std::vector<ListNode*> arr{&n1, &h1, &g1};

    Solution s;
    ListNode* ans = s.mergeKLists(arr);
    while (ans != nullptr) {
        std::cout << ans->val << "->";
        ans = ans->next;
    }
    std::cout << "NULL\n";
    return 0;
}