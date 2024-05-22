#include <bits/stdc++.h>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        size_t n = matrix.size();
        vector<vector<int>> rotated(n, vector<int>(n));

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                rotated[j][n - 1 - i] = matrix[i][j];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matrix[i][j] = rotated[i][j];

        return;
    }
};

int main()
{
    vector<vector<vector<int>>> tests = {
        {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},                               //{{7,4,1},{8,5,2},{9,6,3}}
        {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}}, //{{15,13,2,5},{14,3,4,1},{12,6,8,9},{16,7,10,11}}
    };

    Solution sol;
    for (vector<vector<int>> test : tests)
    {
        sol.rotate(test);
        cout << endl;
        for (vector<int> row : test)
        {
            for (int elem : row)
                cout << elem << " ";
            cout << endl;
        }
    }
}