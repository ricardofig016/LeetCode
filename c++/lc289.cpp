#include <bits/stdc++.h>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    void gameOfLife(vector<vector<int>> &board)
    {
        size_t m = board.size();
        size_t n = board[0].size();

        vector<vector<int>> neighbours(m, vector<int>(n)); // ((row,col),neighbours)

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                neighbours[i][j] = (this->numberOfNeighbours(board, m, n, i, j));

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == 0 && neighbours[i][j] == 3)
                    board[i][j] = 1;
                else if (board[i][j] == 1 && (neighbours[i][j] < 2 || neighbours[i][j] > 3))
                    board[i][j] = 0;
            }
        return;
    }

    int numberOfNeighbours(vector<vector<int>> &board, size_t m, size_t n, int i, int j)
    {
        int neighbours = 0;

        vector<vector<int>> candidates = {
            {i - 1, j - 1},
            {i, j - 1},
            {i + 1, j - 1},
            {i - 1, j},
            {i + 1, j},
            {i - 1, j + 1},
            {i, j + 1},
            {i + 1, j + 1},
        };

        for (vector<int> candidate : candidates)
        {
            int row = candidate[0];
            int col = candidate[1];
            if (row >= 0 && col >= 0 && row < m && col < n && board[row][col] == 1)
                neighbours++;
        }

        return neighbours;
    }
};

int main()
{
    vector<vector<vector<int>>> tests = {
        {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}}, //{{0,0,0},{1,0,1},{0,1,1},{0,1,0}}
        {{1, 1}, {1, 0}},                             //{{1,1},{1,1}}
    };

    Solution sol;
    for (vector<vector<int>> test : tests)
    {
        sol.gameOfLife(test);
        cout << endl;
        for (vector<int> row : test)
        {
            for (int elem : row)
                cout << elem << " ";
            cout << endl;
        }
    }
}