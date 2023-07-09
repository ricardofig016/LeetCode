#include <vector>

using namespace std;

class RandomizedSet {
public:
    vector<int> set;

    RandomizedSet() {
        set = {};
    }
    
    bool insert(int val) {
        set.push_back(val);
    }
    
    bool remove(int val) {
        set.
    }
    
    int getRandom() {
        
    }
};

int main() {
    RandomizedSet* obj = new RandomizedSet();
    bool param_1 = obj->insert(12);
    bool param_1 = obj->insert(15);
    bool param_2 = obj->remove(12);
    int param_3 = obj->getRandom();
    return 0;
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */