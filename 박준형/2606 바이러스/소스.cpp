#include <iostream>
#include <vector>
using namespace std;

vector<bool> visited; // �� ����� �湮 ���θ� �����ϴ� ����
vector<vector<int>> adj; // �׷����� ���� ����Ʈ ǥ��

void dfs(int node) {
    visited[node] = true; // ���� ��带 �湮�ߴٰ� ǥ��
    
   // cout << "Visited " << node << endl;
    
    // ���� ����� ��� �̿��� ����
    for (auto neighbour : adj[node]) {
        // ���� �̿� ��带 ���� �湮���� �ʾҴٸ�
        if (!visited[neighbour]) {
            dfs(neighbour); // �̿� ��� �湮
        }
    }
}

int main() {
    int n;
    int m;
    cin >> n;
    cin >> m;
    visited.resize(n + 1, false); // ��� ��带 �湮���� ���� ���·� �ʱ�ȭ
    adj.resize(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // ������ �׷������ �� ������ �ʿ�
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
