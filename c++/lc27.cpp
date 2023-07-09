#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for(int i = nums.size()-1; i >= 0; i--) {
            if(nums[i] != val) k++;
            else nums.erase(nums.begin() + i);
        }
        for(int i : nums) {
            cout << i << ", ";
        }
        return k;
    }
};

int main() {
    vector<int> nums = {3,2,2,3};
    int val = 3;
    Solution sol;
    cout << sol.removeElement(nums, val) << endl;

    return 0;
}