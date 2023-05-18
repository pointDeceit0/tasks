#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int prevEnd = intervals[0][1];
        int res = 0;

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= prevEnd) {
                prevEnd = intervals[i][1];
            } else {
                res++;
                prevEnd = min(intervals[i][1], prevEnd);
            }
        }
        return res;
    }
};