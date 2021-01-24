#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    map <string, int> m;
    
    for (auto a : completion)
        m[a]++;
    
    for (auto a : participant)
        m[a]--;
    
    for (auto a : participant)
        if(m[a])
            return a;
}