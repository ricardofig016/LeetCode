#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int len = static_cast<int>(nums.size());
        int current_index = 0;
        int jump_count = 0;
        while(current_index < len - 1) {
            int jump_profit = 0;
            int best_jump;
            for(int i = 1; i <= nums[current_index]; i++) {
                if(nums[current_index] + current_index >= len - 1) return jump_count + 1;
                if(nums[current_index + i] + i > jump_profit) {
                    jump_profit = nums[current_index + i] + i;
                    best_jump = i;
                }
            }
            current_index += best_jump;
            jump_count++;
        }
        return jump_count;
    }
};