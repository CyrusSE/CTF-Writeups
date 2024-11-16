#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<vector<int>> pos(10001);  
    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        pos[x].push_back(i);
    }
    
    long long count = 0;
    for(int div = 1; div <= 10000; div++) {
        vector<int>& div_pos = pos[div];
        for(int mul = div; mul <= 10000; mul += div) {
            if(!div_pos.empty() && !pos[mul].empty()) {
                for(int p1 : div_pos) {
                    count += lower_bound(pos[mul].begin(), pos[mul].end(), p1+1) 
                            - pos[mul].begin() < pos[mul].size() ? 
                            pos[mul].end() - lower_bound(pos[mul].begin(), pos[mul].end(), p1+1) : 0;
                }
            }
        }
    }
    
    cout << count << "\n";
    return 0;
}