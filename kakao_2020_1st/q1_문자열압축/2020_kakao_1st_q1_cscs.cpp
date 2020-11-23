#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
	int min = s.size();

	for (int len = 1; len < s.size() / 2 + 1; len++)
	{
		int ts = s.size();

		for (int i = 0; i < s.size() - len; i += len)
		{
			string str = s.substr(i, len);

			int cnt = 0;
			for (int k = i + len; k < s.size(); k += len)
			{
				if (str == s.substr(k, len))
				{
					i += len;
					cnt++;
				}
				else
					break;
			}

			if (cnt)
				ts -= len * cnt - to_string(cnt + 1).size();
		}

		if (min > ts)
			min = ts;
	}

	return min;
}