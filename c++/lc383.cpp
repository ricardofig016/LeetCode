#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> availableChars;
        for (char ch : magazine)
        {
            if (availableChars.find(ch) != availableChars.end())
                availableChars[ch]++;
            else
                availableChars[ch] = 1;
        }

        for (char ch : ransomNote)
        {
            if (availableChars.find(ch) == availableChars.end() || availableChars[ch] == 0)
                return false;
            else
                availableChars[ch]--;
        }

        return true;
    }
};

int main()
{
    vector<vector<string>> tests = {
        {"a", "b"},    // false
        {"aa", "ab"},  // false
        {"aa", "aab"}, // true
    };

    Solution sol;

    for (vector<string> test : tests)
    {
        string ransomNote = test[0];
        string magazine = test[1];

        cout << sol.canConstruct(ransomNote, magazine) << endl;
    }
}