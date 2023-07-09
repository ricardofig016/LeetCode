#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = (int)citations.size();
        sort(citations.begin(),citations.end());
        if(citations[0] >= n) return n;
        if(n == 1) return !(citations[0] == 0);
        for(int i = 0; i < n; i++) {
            int left = n - i;
            if(citations[i] >= left) return left;
        }
        return 0;        
    }
};

int main() {
    vector<int> citations = {1,1,3};
    Solution s;
    cout << s.hIndex(citations) << endl;
    return 0;
}