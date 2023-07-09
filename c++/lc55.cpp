#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int momentum = 0;
        for (int i = 0; i < nums.size(); i++) {
            momentum--;
            if (nums[i] > momentum) momentum = nums[i];
            if (i != nums.size() - 1 && momentum == 0) return false;
        }
        return true;
    }
};