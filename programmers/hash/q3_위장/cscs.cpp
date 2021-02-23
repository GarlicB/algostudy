#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    map<string, int> map;
    
    for (auto a : clothes)
        map[a[1]]++;
        
    int mul = 1;

	for (auto iter = map.begin(); iter != map.end(); iter++)
		mul *= iter->second + 1;

	return mul - 1;
}