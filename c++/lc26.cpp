#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countNotZeros(vector<int>& nums) {
        int k = 0;
        for(int i = 0; i < static_cast<int>(nums.size()); i++) {
            k++;
        }
        return k;
    }

    int removeDuplicates(vector<int>& nums) {
        int i = nums.size()-2;
        while(i >= 0) {
            if(nums.size() < 2) return countNotZeros(nums);
            if(nums[i] == nums[i+1]) {
                nums.erase(nums.begin() + i);
            }
            else {
                if(i==0) return countNotZeros(nums);
            }
            i--;
        }
        return countNotZeros(nums);
    }
};

int main() {
    vector<int> nums = {-1,0,0,0,0,3,3};
    Solution sol;
    cout << sol.removeDuplicates(nums) << endl;
}