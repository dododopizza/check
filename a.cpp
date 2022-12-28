#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
#define F first
#define S second
long long  MOD = 998244353;
vector<int> color;
vector<vector<int>> vec;
int t = 0;
void dfs(int v){
    color[v] = 1;
    for(auto x: vec[v]){
        if(color[x] == 1) t++;
        else if(color[x] != 2){
            dfs(x);
        }
    }
    color[v] = 2;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    ll p,k;
    cin >> p >> k;
    vec.resize(p);
    color.resize(p);
    for(int i = 1;i <= p;i++){
        color[i-1] = 0;
        if((i * k) % p != 0)
        vec[i-1].push_back((i * k) % p - 1);
    }
    for(int i =0;i < p;i++){
        if(color[i] != 2) dfs(i);
    }
    cout << t;
    return 0;
}