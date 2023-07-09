#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> temp;
        int pt1 = m-1, pt2 = n-1;
        for(int i = 0; i < n+m; i++) {
            if(pt2 < 0) {
                temp.insert(temp.begin(), nums1[pt1]);
                pt1--;
                continue;
            }
            if(pt1 < 0) {
                temp.insert(temp.begin(), nums2[pt2]);
                pt2--;
                continue;
            }
            if(nums1[pt1] > nums2[pt2]) {
                temp.insert(temp.begin(), nums1[pt1]);
                pt1--;
                continue;
            } 
            if(nums1[pt1] <= nums2[pt2]) {
                temp.insert(temp.begin(), nums2[pt2]);
                pt2--;
                continue;
            } 
        }
        nums1 = temp;
        for(int i : nums1) {
            cout << i << ", ";
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1};
    int m = 1;
    vector<int> nums2 = {};
    int n = 0;
    
    sol.merge(nums1, m, nums2, n);
}