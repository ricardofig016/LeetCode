#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int,int> num_count; // <number, count>
        for(int i = 0; i < static_cast<int>(nums.size()); i++) {
            if(num_count.find(nums[i]) == num_count.end()) { // nums[i] is not in num_count
                num_count[nums[i]] = 1;
            } else if(num_count[nums[i]] < 2) {
                num_count[nums[i]]++;
            } else if(num_count[nums[i]] >= 2) {
                nums.erase(nums.begin() + i);
                i--;
            }
        }
        return static_cast<int>(nums.size());
    }
};