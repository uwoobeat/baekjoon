#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAX 5000001

int n;
string s;
bool visited[MAX];
vector<int> dq;
vector<vector<int>> tree(MAX);
vector<vector<int>> cand;
vector<string> res;
int max_depth = 1;

void dfs(int v, int depth, int map_depth) {
    for (auto &i : tree[v]) {
        if (visited[i] == false) {
            visited[i] = 1;
            dq.push_back(i);
            dfs(i,depth+1, max_depth);
            max_depth = depth + 1;
            dq.pop_back();
        }
    }
    if (depth >= max_depth) {
        vector<int> tmp(dq);
        cand.push_back(dq);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    cin >> s;
    visited[1] = true;
    dq.push_back(1);

    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    for (auto &i : tree)
        sort(i.begin(), i.end());

    dfs(1, 1, max_depth);

    for (auto& i : cand) {
        string tmp;
        for (auto& j : i) {
            tmp += s[j-1];
        }
        res.push_back(tmp);
    }

    sort(res.begin(), res.end(), greater<string>());
    cout << res[0];
}