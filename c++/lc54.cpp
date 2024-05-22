#include <bits/stdc++.h>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        int row_slide = matrix[0].size() - 1;
        int col_slide = matrix.size() - 1;

        vector<int> result = matrix[0]; // first slide

        pair<int, int> pointer = make_pair(0, row_slide);

        int next_direction = 1; // down

        while (row_slide > 0 && col_slide > 0)
        {
            /*cout << endl
                 << "new slilde:" << endl
                 << "curr pointer: <" << pointer.first << ", " << pointer.second << ">" << endl
                 << "row_slide: " << row_slide << endl
                 << "col_slide: " << col_slide << endl;*/
            if (next_direction == 1 || next_direction == 3)
            {
                for (int i = 0; i < col_slide; i++)
                {
                    if (next_direction == 1) // down
                        pointer.first += 1;
                    else
                        pointer.first -= 1;
                    result.push_back(matrix[pointer.first][pointer.second]);
                }
                col_slide -= 1;
            }
            else
            {
                for (int i = 0; i < row_slide; i++)
                {
                    if (next_direction == 0) // right
                        pointer.second += 1;
                    else
                        pointer.second -= 1;
                    result.push_back(matrix[pointer.first][pointer.second]);
                }
                row_slide -= 1;
            }
            next_direction = (next_direction + 1) % 4;
        }

        // last slide
        /*cout << endl
             << "last slilde:" << endl
             << "curr pointer: <" << pointer.first << ", " << pointer.second << ">" << endl
             << "row_slide: " << row_slide << endl
             << "col_slide: " << col_slide << endl
             << "direction: " << next_direction << endl;*/
        switch (next_direction)
        {
        case 0: // right
            for (int i = 0; i < row_slide; i++)
            {
                pointer.second += 1;
                result.push_back(matrix[pointer.first][pointer.second]);
            }
            break;
        case 1: // down
            for (int i = 0; i < col_slide; i++)
            {
                pointer.first += 1;
                result.push_back(matrix[pointer.first][pointer.second]);
            }
            break;
        case 2: // left
            for (int i = 0; i < row_slide; i++)
            {
                pointer.second -= 1;
                result.push_back(matrix[pointer.first][pointer.second]);
            }
            break;
        case 3: // up
            for (int i = 0; i < col_slide; i++)
            {
                pointer.first -= 1;
                result.push_back(matrix[pointer.first][pointer.second]);
            }
            break;
        default:
            break;
        }

        return result;
    }
};

int main()
{
    vector<vector<vector<int>>> matrixes =
        {
            {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
            {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}},
        };

    Solution sol;

    for (vector<vector<int>> matrix : matrixes)
    {
        vector<int> result = sol.spiralOrder(matrix);
        for (int num : result)
        {
            cout << num << " ";
        }
        cout << endl;
    }
}