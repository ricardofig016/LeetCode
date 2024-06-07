class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        unordered_map<char, char> sMap;
        unordered_map<char, char> tMap;
        for (int i = 0; i < s.length(); i++)
        {
            if (sMap.find(s[i]) != sMap.end() && sMap[s[i]] != t[i])
                return false;
            if (tMap.find(t[i]) != tMap.end() && tMap[t[i]] != s[i])
                return false;
            sMap[s[i]] = t[i];
            tMap[t[i]] = s[i];
        }

        return true;
    }
};