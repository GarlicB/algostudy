#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(int a, int b) {
    return a > b;
}

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = 0;
    
    sort(dist.begin(), dist.end(), cmp);
    
    vector<int> d;
    
    for (int i = 1; i <= dist.size(); i++)
    {
        d.push_back(dist[i-1]);
        
        do
        {
            // for(auto a : d)
            //     cout << a << " ";
            // cout << endl;

            for (int s = 0; s < weak.size() ; s++)
            {
                vector<int> v;

                for(int r = s; r < weak.size(); r++)
                    v.push_back(weak[r]);

                for(int l = 0; l < s; l++)
                    v.push_back(weak[l]+n);

                // for (auto a : v)
                //     cout << a << " ";
                // cout << endl;

                int n = 0, m = 0;
                while(n < v.size() && m < d.size())
                {
                    // cout << n << " " << m << " ";
                    int c = v[n] + d[m];
                    while(n < v.size() && v[n] <= c) n++;
                    m++;
                    // cout << c << endl;
                }

                if(n >= v.size())
                    return i;
            }
        } while(prev_permutation(d.begin(), d.end()));
    }
    
    return -1;
}