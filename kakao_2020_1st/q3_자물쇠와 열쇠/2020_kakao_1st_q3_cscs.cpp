#include <string>
#include <vector>
#include <iostream>

using namespace std;

int k, l, r;

int check(vector<vector<int>> map, vector<vector<int>> key, int y, int x)
{
    for(int i = y; i < k+y; i++)
        for(int j = x; j < k+x; j++)
            map[i][j] += key[i-y][j-x];
    
    for (int i = k-1; i < l+k-1; i++)
        for(int j = k-1; j < l+k-1; j++)
            if(map[i][j] != 1)
                return false;
    
    return 1;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    k = key.size();
    l = lock.size();
    r = 2*(k-1) + l;
    
    vector<vector<int>> map(r, vector<int> (r, 0));
    vector<vector<int>> key2(r, vector<int> (r, 0));
    
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < r; j++)
            if(i <= k-2 || i >= k-1+l || j <= k-2 || j >= k-1+l)
                continue;
            else
                map[i][j] = lock[i-k+1][j-k+1];
    }
    
    if(check(map, key2, r-k, r-k))
        return true;
    
    for (int z = 0; z < 4; z++)
    {
        for (int i = 0; i < k; i++)
            for (int j = 0; j < k; j++)
                key2[j][k-1-i] = key[i][j];
        
        for (int i = 0; i < k; i++)
            for (int j = 0; j < k; j++)
                key[i][j] = key2[i][j];
        
        for (int i = 0; i <= r - k; i++)
        {
            for (int j = 0; j <= r - k; j++)
                if(check(map, key2, i, j))
                    return true;
        }
    }
    
    return false;
}