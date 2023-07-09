#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int len = static_cast<int>(nums.size());
        k = k%len;
        vector<int> temp;
        for(int i = len - k; i < len; i++)  {
            temp.push_back(nums[i]);
        }
        for(int i = 0; i < len - k; i++) {
            temp.push_back(nums[i]);
        }
        nums = temp;

        for(int n : nums) {
            cout << n << ", ";
        }      
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-1};
    sol.rotate(nums, 3);
}