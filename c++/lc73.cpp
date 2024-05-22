#include <bits/stdc++.h>
#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        size_t m = matrix.size();
        size_t n = matrix[0].size();

        vector<pair<int, int>> no_set_coords;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
            {
                if (matrix[i][j] == 0 and !this->pairIsInVector(make_pair(i, j), no_set_coords))
                {
                    setZeroesRow(matrix, i, n, no_set_coords);
                    setZeroesCol(matrix, j, m, no_set_coords);
                }
            }

        return;
    }

    bool pairIsInVector(pair<int, int> q, vector<pair<int, int>> &v)
    {
        for (pair<int, int> e : v)
            if (e == q)
                return true;
        return false;
    }

    void setZeroesRow(vector<vector<int>> &matrix, int &row, size_t &n, vector<pair<int, int>> &no_set_coords)
    {
        for (int j = 0; j < n; j++)
        {
            if (matrix[row][j] != 0)
            {
                matrix[row][j] = 0;
                no_set_coords.push_back(make_pair(row, j));
            }
        }
        return;
    }

    void setZeroesCol(vector<vector<int>> &matrix, int &col, size_t &m, vector<pair<int, int>> &no_set_coords)
    {
        for (int i = 0; i < m; i++)
        {
            if (matrix[i][col] != 0)
            {
                matrix[i][col] = 0;
                no_set_coords.push_back(make_pair(i, col));
            }
        }
        return;
    }
};

int main()
{
    vector<vector<vector<int>>> tests = {
        {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}},          //{{1,0,1},{0,0,0},{1,0,1}}
        {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}}, // {{0,0,0,0},{0,4,5,0},{0,3,1,0}}
    };

    Solution sol;
    for (vector<vector<int>> test : tests)
    {
        sol.setZeroes(test);
        cout << endl;
        for (vector<int> row : test)
        {
            for (int elem : row)
                cout << elem << " ";
            cout << endl;
        }
    }
}