#include <iostream>
#include <vector>
using namespace std;

vector<bool> visited; // 각 노드의 방문 여부를 저장하는 벡터
vector<vector<int>> adj; // 그래프의 인접 리스트 표현

void dfs(int node) {
    visited[node] = true; // 현재 노드를 방문했다고 표시
    
   // cout << "Visited " << node << endl;
    
    // 현재 노드의 모든 이웃에 대해
    for (auto neighbour : adj[node]) {
        // 만약 이웃 노드를 아직 방문하지 않았다면
        if (!visited[neighbour]) {
            dfs(neighbour); // 이웃 노드 방문
        }
    }
}

int main() {
    int n;
    int m;
    cin >> n;
    cin >> m;
    visited.resize(n + 1, false); // 모든 노드를 방문하지 않은 상태로 초기화
    adj.resize(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // 무방향 그래프라면 이 라인이 필요
    }
    dfs(1);
    
    int count=0;
    for (int i = 1; i <= n; i++) {
        if (visited[i]) {
            count++;
        }
    }
    cout << count-1;
}
