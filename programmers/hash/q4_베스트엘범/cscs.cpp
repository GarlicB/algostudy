#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b)
{
	if (a.second > b.second)
		return true;
	else
		return false;
}

bool cmp2(pair<string, int>& a, pair<string, int>& b)
{
	if (a.second > b.second)
		return true;
	else
		return false;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    
    map<string, vector<pair<int, int>>> m;
	map<string, int> m2;
    
	for(int i = 0; i < genres.size(); i++)
	{
		m[genres[i]].push_back(make_pair(i, plays[i]));
		m2[genres[i]] += plays[i];
	}
    
    for(auto iter = m.begin(); iter != m.end(); iter++)
		sort(iter->second.begin(), iter->second.end(), cmp);

	vector<int> v;
	int maxc = 2;
    
    vector<pair<string, int>> v2;
	for (auto iter = m2.begin(); iter != m2.end(); iter++)
		v2.push_back(make_pair(iter->first, iter->second));
	sort(v2.begin(), v2.end(), cmp2);

	for (auto a : v2)
	{
		int c = m[a.first].size() >= maxc ? maxc : m[a.first].size();
		
		for(int i = 0; i < c; i++)
			v.push_back(m[a.first][i].first);
	}

	return v;
}