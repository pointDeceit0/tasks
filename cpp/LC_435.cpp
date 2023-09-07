#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end());

        int ans = 0;
        int prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (prevEnd > intervals[i][0]) {
                ans++;
                prevEnd = std::min(prevEnd, intervals[i][1]);
            }
            else {
                prevEnd = intervals[i][1];
            }
        }

        return ans++;
    }
};

int main() {
    Solution s;
    std::vector<std::vector<int>> inp {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
    std::cout << s.eraseOverlapIntervals(inp) << " 1\n";

    inp = {{1, 2}, {1, 2}, {1, 2}};
    std::cout << s.eraseOverlapIntervals(inp) << " 2\n";

    inp = {{1, 2}, {2, 3}};
    std::cout << s.eraseOverlapIntervals(inp) << " 0\n";

    inp = {{2, 3}, {3, 4}, {1, 8}, {5, 6}, {7, 9}, {8, 9}};
    std::cout << s.eraseOverlapIntervals(inp) << " 2\n";
    return 0;
}