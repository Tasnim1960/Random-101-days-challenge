#include<bits/stdc++.h>
using namespace std;

class Edge
{
public:
    int source;
    int destination;
    int weight;
};

class Graph
{
public:
    int V;
    int E;
    Edge * edges;

    Graph(int V,int E)
    {
        this->V=V;
        this->E=E;
        edges = new Edge[E];

    }

    void addEdge(int c, int u,int v, int w)
    {
        edges[c].source=u;
        edges[c].destination=v;
        edges[c].weight=w;

    }

};

 void printGraph(Graph* graph)
    {

        for(int j=0; j<graph->E; j++)
        {

            cout<<"("<<graph->edges[j].source<<" "<<graph->edges[j].destination<<" "<<graph->edges[j].weight<<")"<<endl;

        }

    }

void BellmanFord( Graph* graph, int src)

{

    int V = graph->V;

    int E = graph->E;

    int *dist = new int[V];

    // Step 1: Initialize distances from src to all other vertices as INFINITE

    for (int i = 0; i < V; i++)

        dist[i]   = INT_MAX;

    dist[src] = 0;

    // Step 2: Relax all edges |V| - 1 times. A simple shortest path from src

    // to any other vertex can have at-most |V| - 1 edges

    for (int i = 1; i <= V-1; i++)

    {

        for (int j = 0; j < E; j++)

        {

            int u = graph->edges[j].source;

            int v = graph->edges[j].destination;

            int weight = graph->edges[j].weight;

            if (dist[u] + weight < dist[v])

                dist[v] = dist[u] + weight;
        }

    }

    for (int i = 0; i < E; i++)

    {
        int u = graph->edges[i].source;

        int v = graph->edges[i].destination;

        int weight = graph->edges[i].weight;

        if (dist[u] + weight < dist[v])

            printf("Graph contains negative weight cycle\n");

    }


 printf("Vertex   Distance from Source\n");
    for (int i = 0; i < V; ++i)

        printf("%d \t\t %d\n", i, dist[i]);

}
int main()

{

    /* Let us create the graph given in above example */

    int v; // Number of vertices in graph

    int e;  // Number of edges in graph

    cin>>v>>e;

    Graph *G = new Graph(v,e);

    int u1,v1,w;
    for(int i=0; i<e; i++)
    {
        cin>>u1>>v1>>w;
        G->addEdge(i,u1,v1,w);
    }
    printGraph(G);
    BellmanFord(G,0);


    return 0;}

