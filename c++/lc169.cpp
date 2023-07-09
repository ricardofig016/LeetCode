#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        if(n == 1) return nums[0];
        sort(nums.begin(), nums.end());
        int counter = 1;
        for(int i = 0; i<n-1; i++) {
            if(nums[i] == nums[i+1]) {
                counter++;
                if(counter > n/2) return nums[i];
            }
            else {
                counter = 1;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2,2,1,1,1,2,2};
    cout << sol.majorityElement(nums) << endl;
}