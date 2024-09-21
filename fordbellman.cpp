#include <iostream>
#include <vector>

using namespace std;

const int MAX = 101;

void minSpanningTree(vector<vector<int>>& graph, int start) {
    int* dist = new int[graph.size()];
    int m = 1;
    for (int i = 0; i < graph.size(); i++) 
        dist[i] = MAX;

    dist[start] = 0;

    cout << "D[0] = ";
    for (int i = 0; i < graph.size(); i++)
        cout << dist[i] << " ";
    cout << endl;

    while (1) {
        int* d = new int[graph.size()];
        int k = 0;

        for (int i = 0; i < graph.size(); i++) {
            int min = MAX;
            for (int j = 0; j < graph.size(); j++) {
                if (min > dist[j] + graph[j][i])
                    min = dist[j] + graph[j][i];
            }
            d[i] = min;
        }

        cout << "D[" << m << "] = ";
        for (int i = 0; i < graph.size(); i++) {
            if (i != start) {
                if (dist[i] > d[i]) {
                    dist[i] = d[i];
                    k++;
                }
                cout << dist[i] << " ";
            }
        }
        cout << endl;

        m++;

        if (k == 0)
            break;
    }
}

int main() {
    /*srand(time(NULL));
    int V = 6;
    vector<vector<int>> graph(V, vector<int>(V));

    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            if (i == j)
                graph[i][j] = 0;
            else if (j < i)
                graph[i][j] = graph[j][i];
            else
                graph[i][j] = rand() % 100 + 1;
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }*/
    vector<vector<int>> graph = {
        {0, 2, 7, 4, 6, 3},
        {3, 0, 4, 5, 6, 1},
        {2, 4, 0, 8, 7, MAX},
        {4, MAX, 8, 0, 5, 7},
        {MAX, 7, 8, 4, 0, 3},
        {2, 4, MAX, 7, 8, 0}
    };

    minSpanningTree(graph, 3);

    return 0;
}
