#include <iostream>
#include <vector>
using namespace std;

#define N 100

struct node {
    int val;
    int cost;
};

vector<node> G[N];

int main() {

    int nodes;
    int edges;
    cin >> nodes >> edges;

    for (int i = 0; i < edges; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        G[u].push_back({v, w});
        // If graph is undirected, also add:
        // G[v].push_back({u, w});
    }

    for (int i = 0; i < nodes; i++) {
        cout << i << " ";
        for (int j = 0; j < G[i].size(); j++) {
            cout << "{" << G[i][j].val << "," << G[i][j].cost << "} ";
        }
        cout << endl;
    }

    return 0;
}
