#include <bits/stdc++.h>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    string minWindow(string &s, string &t)
    {
        int m = s.size();
        int n = t.size();

        vector<int> char_count(123, 0); // 122 is the ascii code for 'z'
        for (char c : t)
        {
            char_count[c]++;
        }

        int best_start_index = 0;
        int min_length = __INT_MAX__;
        int missing_in_sub_s = n;

        int w_start = 0;
        int w_end = 0;

        while (w_end < m)
        {
            if (char_count[s[w_end]] > 0)
            {
                missing_in_sub_s--;
            }
            char_count[s[w_end]]--;
            w_end++;

            while (!missing_in_sub_s)
            {
                if (w_end - w_start < min_length)
                {
                    best_start_index = w_start;
                    min_length = w_end - w_start;
                }

                if (char_count[s[w_start]] == 0)
                    missing_in_sub_s++;
                char_count[s[w_start]]++;
                w_start++;
            }
        }
        return min_length == __INT_MAX__ ? "" : s.substr(best_start_index, min_length);
    }
};

int main()
{
    vector<vector<string>> tests = {
        {"ADOBECODEBANC", "ABC"}, // "BANC"
        {"a", "a"},               // "a"
        {"a", "aa"},              // ""
    };
    Solution sol;
    for (vector<string> test : tests)
    {
        cout << sol.minWindow(test[0], test[1]) << endl;
    }
}