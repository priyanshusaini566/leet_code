#include<bits/stdc++.h>
using namespace std;
void primsAlgo(vector<vector<int>> graph[],int V,int stNode){
    priority_queue<pair<int, int>,vector<pair<int, int>>,greater<pair<int, int>>>pq;
    vector<bool> visited(V,false);

    pq.push({0,stNode});
    int minCost=0;

    while(!pq.empty()){
        int u=pq.top().second;
        int wt=pq.top().first;

        if(visited[u]){
            continue;

        }
        visited[u]=true;
        minCost =+ wt;

        for(auto &neighbour: graph[u]){
            int v= neighbour[0];
            int weight=neighbour[1];
            if(!visited[v]){
                pq.push({weight,v});

            }
        }
    }
    return minCost;


}

int main(){
    int V,E;
    cout<<"Enter number of Vertices: ";

    cout<<"Enter number of Edges: ";
    cin>>E;

    //Array of vector
    vector<vector<int>>graph[V];

    for(int i=0;i<E;i++){
        int u,v,w;
        cin>>u>>v>>w;

        //undirected graph
        graph[u].push_back({v,w});
        graph[v].push_back({u,w});
        }

    for(int i=0;i<V;i++){
        cout<<i<<": ";

    }
    int stNode;
    cout<<"Enter starting Node:";
    cin>>stNode;

    cout<<"MST cost"

}