#include <string>
#include <vector>
#include <iostream>

using namespace std;

int check(string str)
{
	if (str.size() == 0)
		return 0;

	vector<char> s;

	s.push_back(str[0]);
	for (auto a : str.substr(1, str.size() + 1))
	{
		if (s.back() == '(' && a == ')')
			s.pop_back();
		else
			s.push_back(a);
	}

	if (s.size() == 0)
		return 1;
	return 0;
}

string rec(string w)
{
	if (w.empty())
		return "";

	if (check(w))
		return w;

	int l = 0, r = 0;

	for (auto a : w)
	{
		if (a == '(') l++;
		else r++;

		if (l == r && l + r >= 2)
			break;
	}

	string u = w.substr(0, l + r);
	string v = w.substr(l + r, w.size() + 1);

	if (check(u))
		return u + rec(v);
	else
	{
		string x = "(" + rec(v) + ")";
		string y = "";

		if (u.size() > 2)
		{
			y = u.substr(1, u.size() - 2);
			for (auto& a : y)
				if (a == '(') a = ')';
				else a = '(';
		}

		return x + y;
	}
}

string solution(string p) {
	string answer = "";

	answer = rec(p);

	return answer;
}